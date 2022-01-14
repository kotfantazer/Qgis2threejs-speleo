# -*- coding: utf-8 -*-
"""
/***************************************************************************
 keyframes.py

                              -------------------
        begin                : 2021-11-10
        copyright            : (C) 2021 Minoru Akagi
        email                : akaginch@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QDialog, QInputDialog, QMenu, QMessageBox,
                             QTreeWidget, QTreeWidgetItem, QWidget)
from qgis.core import QgsApplication

from .conf import DEBUG_MODE, DEF_SETS
from .q3dconst import LayerType, ATConst
from .q3dcore import Layer
from .tools import createUid, logMessage
from .ui.animationpanel import Ui_AnimationPanel
from .ui.keyframedialog import Ui_KeyframeDialog


class AnimationPanel(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.isAnimating = False

        self.ui = Ui_AnimationPanel()
        self.ui.setupUi(self)
        self.ui.treeWidgetAnimation = AnimationTreeWidget(self)
        self.ui.treeWidgetAnimation.setObjectName("treeWidgetAnimation")
        self.ui.verticalLayout.addWidget(self.ui.treeWidgetAnimation)

        self.tree = self.ui.treeWidgetAnimation

    def setup(self, wnd, settings):
        self.wnd = wnd
        self.webPage = wnd.webPage

        self.ui.toolButtonAdd.setIcon(QgsApplication.getThemeIcon("symbologyAdd.svg"))
        self.ui.toolButtonEdit.setIcon(QgsApplication.getThemeIcon("symbologyEdit.svg"))
        self.ui.toolButtonRemove.setIcon(QgsApplication.getThemeIcon("symbologyRemove.svg"))

        self.ui.toolButtonAdd.clicked.connect(self.tree.addNewItem)
        self.ui.toolButtonEdit.clicked.connect(self.tree.showDialog)
        self.ui.toolButtonRemove.clicked.connect(self.tree.removeCurrentItem)
        self.ui.toolButtonPlay.clicked.connect(self.playButtonClicked)

        self.tree.setup(wnd, settings)

        self.webPage.bridge.animationStopped.connect(self.animationStopped)

    def playButtonClicked(self, _):
        if self.isAnimating:
            self.stopAnimation()
        else:
            self.playAnimation()

    def playAnimation(self, items=None):
        dataList = []
        for item in (items or self.tree.checkedGroups()):

            if item.type() == ATConst.ITEM_GRP_MATERIAL:
                layerId = item.parent().data(0, ATConst.DATA_LAYER_ID)
                layer = self.wnd.settings.getLayer(layerId)
                if layer:
                    layer = layer.clone()
                    layer.opt.onlyMaterial = True
                    layer.opt.allMaterials = True
                    self.wnd.iface.updateLayerRequest.emit(layer)

            data = self.tree.transitionData(item)
            if data:
                dataList.append(data)

        if len(dataList):
            if DEBUG_MODE:
                logMessage("Play: " + str(dataList))
            self.wnd.iface.requestRunScript("startAnimation(pyData());", data=dataList)
            self.ui.toolButtonPlay.setText("Stop")
            self.isAnimating = True

    def stopAnimation(self):
        self.webPage.runScript("stopAnimation();")

    # @pyqtSlot()
    def animationStopped(self):
        self.ui.toolButtonPlay.setText("Play")
        self.isAnimating = False

    def updateKeyframeView(self):
        view = self.webPage.cameraState(flat=True)

        msg = "Are you sure you want to update the camera position and focal point of this keyframe?"
        if QMessageBox.question(self, "Qgis2threejs", msg) == QMessageBox.Yes:
            item = self.tree.currentItem()
            item.setData(0, ATConst.DATA_CAMERA, view)


class AnimationTreeWidget(QTreeWidget):

    def __init__(self, parent):
        QTreeWidget.__init__(self, parent)

        self.panel = parent

        root = self.invisibleRootItem()
        root.setFlags(root.flags() & ~Qt.ItemIsDropEnabled)

        self.header().setVisible(False)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.setExpandsOnDoubleClick(False)

    def setup(self, wnd, settings):
        self.wnd = wnd
        self.webPage = wnd.webPage

        self.settings = settings

        self.icons = wnd.icons
        self.cameraIcon = QgsApplication.getThemeIcon("mIconCamera.svg")
        self.keyframeIcon = QgsApplication.getThemeIcon("mItemBookmark.svg")

        self.setData(settings.animationData())

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)
        self.currentItemChanged.connect(self.currentTreeItemChanged)
        self.doubleClicked.connect(self.showDialog)

        # context menu
        self.actionNewGroup = QAction("New Group", self)
        self.actionNewGroup.triggered.connect(self.addNewItem)

        self.actionAdd = QAction("Add...", self)        # NOTE: might be hidden
        self.actionAdd.triggered.connect(self.addNewItem)

        self.actionRemove = QAction("Remove...", self)
        self.actionRemove.triggered.connect(self.removeCurrentItem)

        self.actionEdit = QAction("Edit...", self)
        self.actionEdit.triggered.connect(self.showDialog)

        self.actionPlay = QAction("Play", self)
        self.actionPlay.triggered.connect(self.panel.playAnimation)

        self.actionUpdateView = QAction("Set current view to this keyframe...", self)
        self.actionUpdateView.triggered.connect(self.panel.updateKeyframeView)

        self.actionOpacity = QAction("Change Opacity...", self)
        self.actionOpacity.triggered.connect(self.addOpacityItem)

        self.actionMaterial = QAction("Change Material...", self)
        self.actionMaterial.triggered.connect(self.addMaterialItem)

        self.actionGrowLine = QAction("Line Growing Effect...", self)
        self.actionGrowLine.triggered.connect(self.addGrowLineItem)

        self.actionProperties = QAction("Properties...", self)
        self.actionProperties.triggered.connect(self.showLayerProperties)

        self.ctxMenuKeyframeGroup = QMenu(self)
        self.ctxMenuKeyframeGroup.addAction(self.actionPlay)
        self.ctxMenuKeyframeGroup.addAction(self.actionAdd)
        self.ctxMenuKeyframeGroup.addSeparator()
        self.ctxMenuKeyframeGroup.addAction(self.actionEdit)
        self.ctxMenuKeyframeGroup.addSeparator()
        self.ctxMenuKeyframeGroup.addAction(self.actionRemove)

        self.ctxMenuKeyframe = QMenu(self)
        self.ctxMenuKeyframe.addAction(self.actionPlay)
        self.ctxMenuKeyframe.addAction(self.actionEdit)
        self.ctxMenuKeyframe.addAction(self.actionUpdateView)
        self.ctxMenuKeyframe.addSeparator()
        self.ctxMenuKeyframe.addAction(self.actionRemove)

        self.ctxMenuLayerAdd = QMenu("Add", self)
        self.ctxMenuLayerAdd.addActions([self.actionOpacity, self.actionMaterial, self.actionGrowLine])

        self.ctxMenuLayer = QMenu(self)
        self.ctxMenuLayer.addMenu(self.ctxMenuLayerAdd)
        self.ctxMenuLayer.addSeparator()
        self.ctxMenuLayer.addAction(self.actionProperties)

    def focusOutEvent(self, event):
        #TODO: restore layer opacity
        return QTreeWidget.focusOutEvent(self, event)

    def initTree(self):
        self.clear()
        self.nextKeyframeGroupId = 1

    def addCameraMotionTLItem(self):
        item = QTreeWidgetItem(self, ["Camera Motion"], ATConst.ITEM_TL_CAMERA)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setIcon(0, self.cameraIcon)
        item.setExpanded(True)
        return item

    def addLayer(self, id_layer):
        if isinstance(id_layer, Layer):
            layer = id_layer
            layerId = id_layer.layerId
        else:
            layerId = id_layer
            layer = self.settings.getLayer(layerId)
            if not layer:
                return

        item = QTreeWidgetItem(self, ["Layer '{}'".format(layer.name)], ATConst.ITEM_TL_LAYER)
        item.setData(0, ATConst.DATA_LAYER_ID, layerId)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setIcon(0, self.icons[layer.type])
        item.setExpanded(True)

        return item

    def checkedGroups(self):
        groups = []
        root = self.invisibleRootItem()
        for i in range(root.childCount()):
            top_level = root.child(i)
            for j in range(top_level.childCount()):
                g = top_level.child(j)
                if g.checkState(0):
                    groups.append(g)
        return groups

    def currentLayer(self):
        item = self.currentItem()
        if item:
            while item.parent():
                item = item.parent()

            return self.getLayerFromLayerItem(item)

    def getLayerFromLayerItem(self, item):
        layerId = item.data(0, ATConst.DATA_LAYER_ID)
        return self.settings.getLayer(layerId)

    def findLayerItem(self, layerId):
        root = self.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i)
            if item.type() == ATConst.ITEM_TL_LAYER and item.data(0, ATConst.DATA_LAYER_ID) == layerId:
                return item

    def setLayerHidden(self, layerId, b=True):
        item = self.findLayerItem(layerId)
        if item:
            item.setHidden(b)

    def addNewItem(self):
        item = self.currentItem()
        if item is None:
            return

        typ = item.type()
        parent = None
        if typ & ATConst.ITEM_TOPLEVEL:
            if typ == ATConst.ITEM_TL_CAMERA:
                parent = self.addKeyframeGroupItem(item, ATConst.ITEM_GRP_CAMERA)
                self.setCurrentItem(self.addKeyframeItem(parent))
            else:
                layer = self.getLayerFromLayerItem(item)
                self.actionMaterial.setVisible(layer.type == LayerType.DEM)
                self.actionGrowLine.setVisible(layer.type == LayerType.LINESTRING)
                self.ctxMenuLayer.popup(QCursor.pos())
            return

        gt = typ if typ & ATConst.ITEM_GRP else typ - ATConst.ITEM_MBR + ATConst.ITEM_GRP
        if gt == ATConst.ITEM_GRP_CAMERA:
            parent = item if typ == ATConst.ITEM_GRP_CAMERA else item.parent()
            self.setCurrentItem(self.addKeyframeItem(parent))

        elif gt == ATConst.ITEM_GRP_OPACITY:
            self.addOpacityItem()

        elif gt == ATConst.ITEM_GRP_MATERIAL:
            self.addMaterialItem()

        # elif gt == ATConst.ITEM_GRP_GROWING_LINE:
        #     self.addGrowLineItem()

    def removeCurrentItem(self):
        item = self.currentItem()
        if item is None or item.parent() is None:
            return

        msg = "Are you sure you want to remove '{}'?".format(item.text(0))
        if QMessageBox.question(self, "Qgis2threejs", msg) != QMessageBox.Yes:
            return

        item.parent().removeChild(item)

    def addKeyframeGroupItem(self, parent, typ, name=None, enabled=True, easing=None):

        item = QTreeWidgetItem(typ)
        item.setText(0, name or "{} {}".format(ATConst.defaultName(typ), self.nextKeyframeGroupId))
        item.setData(0, ATConst.DATA_EASING, easing)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsDropEnabled | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setCheckState(0, Qt.Checked if enabled else Qt.Unchecked)
        # item.setIcon(0, self.cameraIcon)

        parent.addChild(item)
        item.setExpanded(True)

        self.nextKeyframeGroupId += 1

        return item

    def addKeyframeItem(self, parent=None, keyframe=None):
        if parent is None:
            item = self.currentItem()
            if not item:
                return

            t = item.type()
            if t & ATConst.ITEM_MBR:
                parent = item.parent()
                iidx = parent.indexOfChild(item) + 1
            elif t & ATConst.ITEM_GRP:
                parent = item
                iidx = 0
            elif keyframe:
                pass
            else:
                return
        else:
            iidx = 0

        nextIndex = parent.data(0, ATConst.DATA_NEXT_INDEX) or 1

        keyframe = keyframe or {}
        typ = keyframe.get("type", parent.type() - ATConst.ITEM_GRP + ATConst.ITEM_MBR)
        name = keyframe.get("name") or "Keyframe {}".format(nextIndex)

        item = QTreeWidgetItem(typ)
        item.setText(0, name)

        item.setData(0, ATConst.DATA_EASING, keyframe.get("easing"))
        item.setData(0, ATConst.DATA_DURATION, str(keyframe.get("duration", DEF_SETS.ANM_DURATION)))
        item.setData(0, ATConst.DATA_DELAY, str(keyframe.get("delay", 0)))
        nar = keyframe.get("narration")
        if nar:
            item.setData(0, ATConst.DATA_NARRATION, {"id": nar["id"], "text": nar["text"]})

        if typ == ATConst.ITEM_CAMERA:
            item.setData(0, ATConst.DATA_CAMERA, keyframe.get("camera") or self.webPage.cameraState(flat=True))

        elif typ == ATConst.ITEM_OPACITY:
            item.setData(0, ATConst.DATA_OPACITY, keyframe.get("opacity", 1))

        elif typ == ATConst.ITEM_MATERIAL:
            item.setData(0, ATConst.DATA_MTL_ID, keyframe.get("mtlId", ""))
            item.setData(0, ATConst.DATA_EFFECT, keyframe.get("effect", 1))

        elif typ == ATConst.ITEM_GROWING_LINE:
            item.setData(0, ATConst.DATA_FID, keyframe.get("fid"))

        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsEnabled)
        item.setIcon(0, self.keyframeIcon)

        if iidx:
            parent.insertChild(iidx, item)
        else:
            parent.addChild(item)

        parent.setData(0, ATConst.DATA_NEXT_INDEX, nextIndex + 1)

        return item

    def keyframe(self, item=None):
        item = item or self.currentItem()
        if not item or not (item.type() & ATConst.ITEM_MBR):
            return

        duration = str(item.data(0, ATConst.DATA_DURATION))
        delay = str(item.data(0, ATConst.DATA_DELAY))

        k = {
            "type": item.type(),
            "name": item.text(0),
            "duration": int(duration) if duration.isdigit() else 0,
            "delay": int(delay) if delay.isdigit() else 0
        }
        e = item.data(0, ATConst.DATA_EASING)
        if e:
            k["easing"] = e

        n = item.data(0, ATConst.DATA_NARRATION)
        if n:
            k["narration"] = n

        typ = item.type()
        if typ == ATConst.ITEM_CAMERA:
            k["camera"] = item.data(0, ATConst.DATA_CAMERA)

        elif typ == ATConst.ITEM_OPACITY:
            k["opacity"] = item.data(0, ATConst.DATA_OPACITY)

        elif typ == ATConst.ITEM_MATERIAL:
            layer = self.getLayerFromLayerItem(item.parent().parent())
            if layer:
                id = item.data(0, ATConst.DATA_MTL_ID)
                k["mtlId"] = id
                k["mtlIndex"] = layer.mtlIndex(id)
                k["effect"] = item.data(0, ATConst.DATA_EFFECT) or item.parent().data(0, ATConst.DATA_EFFECT) or 1

        elif typ == ATConst.ITEM_GROWING_LINE:
            k["fid"] = item.data(0, ATConst.DATA_FID)

        return k

    def keyframeGroupData(self, item):
        if not item:
            return {}

        typ = item.type()
        if typ & ATConst.ITEM_GRP:
            group = item
        elif typ & ATConst.ITEM_MBR:
            group = item.parent()
        else:
            return {}

        items = [group.child(i) for i in range(group.childCount())]

        d = {
            "type": group.type(),
            "name": group.text(0),
            "enabled": bool(group.checkState(0)),
            "keyframes": [self.keyframe(item) for item in items]
        }

        easing = group.data(0, ATConst.DATA_EASING)
        if easing:
            d["easing"] = easing

        if group.parent().type() == ATConst.ITEM_TL_LAYER:
            layer = self.settings.getLayer(group.parent().data(0, ATConst.DATA_LAYER_ID))
            if layer:
                d["layerId"] = layer.jsLayerId
            else:
                logMessage("[KeyframeGroup] Layer not found in export settings.", error=True)

        return d

    def layerData(self, layer=None):
        if not layer:
            return {}

        layerItem = layer if isinstance(layer, QTreeWidgetItem) else self.findLayerItem(layer)
        if layerItem is None:
            return {}

        items = [layerItem.child(i) for i in range(layerItem.childCount())]

        return {
            "enabled": not layerItem.isDisabled(),
            "groups": [self.keyframeGroupData(item) for item in items]
        }

    def setLayerData(self, layerId, data):
        if layerId is None:
            return

        layerItem = self.findLayerItem(layerId) or self.addLayer(layerId)
        if layerItem is None:
            return

        for _ in range(layerItem.childCount()):
            layerItem.removeChild(layerItem.child(0))

        for group in data.get("groups", []):
            parent = self.addKeyframeGroupItem(layerItem, group.get("type"), group.get("name"), group.get("enabled", True), group.get("easing"))

            for keyframe in group.get("keyframes", []):
                self.addKeyframeItem(parent, keyframe)

    def data(self):
        root = self.invisibleRootItem()
        parent = root.child(0)      # camera motion

        d = {
            "camera": {
                "groups": [self.keyframeGroupData(parent.child(i)) for i in range(parent.childCount())]
            }
        }

        layers = {}
        for item in [root.child(i) for i in range(1, root.childCount())]:
            layers[item.data(0, ATConst.DATA_LAYER_ID)] = self.layerData(item)

        if layers:
            d["layers"] = layers

        return d

    def transitionData(self, item=None):
        item = item or self.currentItem()
        if not item:
            return

        typ = item.type()
        if typ & ATConst.ITEM_MBR:
            parent = item.parent()
            iidx = parent.indexOfChild(item)
            if iidx:
                d = self.keyframeGroupData(parent)
                d["keyframes"] = d["keyframes"][iidx - 1:iidx + 1]
                d["keyframes"][0].pop("narration", None)
                return d

        elif typ & ATConst.ITEM_GRP:
            return self.keyframeGroupData(item)

    def setData(self, data):
        self.initTree()

        # camera motion
        self.cameraTLItem = self.addCameraMotionTLItem()

        for s in data.get("camera", {}).get("groups", []):
            parent = self.addKeyframeGroupItem(self.cameraTLItem, ATConst.ITEM_GRP_CAMERA, s.get("name"), s.get("enabled", True), s.get("easing"))
            for k in s.get("keyframes", []):
                self.addKeyframeItem(parent, k)

        if self.cameraTLItem.childCount() == 0:
            self.addKeyframeGroupItem(self.cameraTLItem, ATConst.ITEM_GRP_CAMERA)

        # layers
        dp = data.get("layers", {})
        for layer in self.settings.layers():
            id = layer.layerId
            self.addLayer(layer)

            d = dp.get(id)
            if d:
                self.setLayerData(id, d)
            self.setLayerHidden(id, not layer.visible)

    def currentItemView(self):
        item = self.currentItem()
        if item and item.type() == ATConst.ITEM_CAMERA:
            return item.data(0, ATConst.DATA_CAMERA)

    def contextMenu(self, pos):
        item = self.itemAt(pos)
        if item is None:
            # blank space
            return

        m = None
        typ = item.type()
        if typ & ATConst.ITEM_TOPLEVEL:
            if typ == ATConst.ITEM_TL_LAYER:
                m = self.ctxMenuLayer

        else:
            if typ & ATConst.ITEM_GRP:
                m = self.ctxMenuKeyframeGroup
                self.actionAdd.setVisible(bool(typ != ATConst.ITEM_GRP_GROWING_LINE))

            elif typ & ATConst.ITEM_MBR:
                m = self.ctxMenuKeyframe
                self.actionUpdateView.setVisible(bool(typ == ATConst.ITEM_CAMERA))

        if m:
            m.exec_(self.mapToGlobal(pos))

    def currentTreeItemChanged(self, current, previous):

        if not current:
            return

        if DEBUG_MODE:
            logMessage("Current: " + str(self.keyframe(current)))

        typ = current.type()
        if not (typ & ATConst.ITEM_MBR):
            return

        if typ == ATConst.ITEM_CAMERA:
            # restore the view of current keyframe
            k = self.keyframe()
            if k:
                self.webPage.setCameraState(k.get("camera") or {})

        elif typ == ATConst.ITEM_OPACITY:
            layerId = current.parent().parent().data(0, ATConst.DATA_LAYER_ID)
            layer = self.settings.getLayer(layerId)
            if layer:
                opacity = current.data(0, ATConst.DATA_OPACITY)
                self.webPage.runScript("setLayerOpacity({}, {})".format(layer.jsLayerId, opacity))

        elif typ == ATConst.ITEM_MATERIAL:
            layerId = current.parent().parent().data(0, ATConst.DATA_LAYER_ID)
            layer = self.settings.getLayer(layerId)
            if layer:
                layer = layer.clone()
                layer.properties["mtlId"] = current.data(0, ATConst.DATA_MTL_ID)
                layer.opt.onlyMaterial = True
                self.wnd.iface.updateLayerRequest.emit(layer)

    def addOpacityItem(self):
        item = self.currentItem()
        if not item:
            return

        val, ok = QInputDialog.getDouble(self, "Layer Opacity", "Opacity (0 - 1)", 1, 0, 1, 2)
        if ok:
            parent = None
            if item.type() == ATConst.ITEM_TL_LAYER:
                parent = self.addKeyframeGroupItem(item, ATConst.ITEM_GRP_OPACITY)

            self.addKeyframeItem(parent, {"type": ATConst.ITEM_OPACITY,
                                          "name": "Opacity '{}'".format(val),
                                          "opacity": val
                                          })

    def addMaterialItem(self):
        item = self.currentItem()
        layer = self.currentLayer()
        if not item or not layer:
            return

        mtlNames = ["[{}] {}".format(i, mtl.get("name", "")) for i, mtl in enumerate(layer.properties.get("materials", []))]

        if not mtlNames:
            QMessageBox.warning(self, "Material", "The layer has no materials.")
            return

        val, ok = QInputDialog.getItem(self, "Material", "Select a material", mtlNames, 0, False)
        if ok:
            mtlIdx = int(val.split("]")[0][1:])
            mtl = layer.properties["materials"][mtlIdx]

            parent = None
            if item.type() == ATConst.ITEM_TL_LAYER:
                parent = self.addKeyframeGroupItem(item, ATConst.ITEM_GRP_MATERIAL)

            self.addKeyframeItem(parent, {
                "type": ATConst.ITEM_MATERIAL,
                "name": "Material '{}'".format(mtl.get("name", "")),
                "mtlId": mtl.get("id")
            })

    def addGrowLineItem(self):
        item = self.currentItem()
        layer = self.currentLayer()
        if not item or not layer:
            return

        parent = None
        if item.type() == ATConst.ITEM_TL_LAYER:
            parent = self.addKeyframeGroupItem(item, ATConst.ITEM_GRP_GROWING_LINE)

        self.addKeyframeItem(parent, {
            "type": ATConst.ITEM_GROWING_LINE,
            "name": "Line Growing Effect"
        })

    def showDialog(self):
        item = self.currentItem()
        if item is None:
            return

        t = item.type()
        if t & ATConst.ITEM_MBR:
            top_level = item.parent().parent()
        elif t & ATConst.ITEM_GRP:
            top_level = item.parent()
        elif t == ATConst.ITEM_TL_LAYER:
            top_level = item
        else:
            return

        layer = None
        if top_level.type() == ATConst.ITEM_TL_LAYER:
            layerId = top_level.data(0, ATConst.DATA_LAYER_ID)
            layer = self.settings.getLayer(layerId)

            if t == ATConst.ITEM_TL_LAYER:
                self.wnd.showLayerPropertiesDialog(layer)
                return

        dialog = KeyframeDialog(self)
        dialog.setup(item, layer)
        dialog.show()
        dialog.exec_()

    def showLayerProperties(self):
        layer = self.currentLayer()
        if layer:
            self.wnd.showLayerPropertiesDialog(layer)


class KeyframeDialog(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_KeyframeDialog()
        self.ui.setupUi(self)

        self.panel = parent.panel
        self.narId = None
        self.isPlaying = self.isPlayingAll = False

        parent.webPage.bridge.tweenStarted.connect(self.tweenStarted)
        parent.webPage.bridge.animationStopped.connect(self.animationStopped)

    def setup(self, item, layer=None):
        self.item = item
        self.itemTo = self.itemFrom = None
        self.type = t = item.type()
        self.layer = layer

        self.setWindowTitle("{} - {}".format(item.parent().text(0), layer.name if layer else "Camera Motion"))

        idx = item.data(0, ATConst.DATA_EASING) or 0
        self.ui.comboBoxEasing.addItems(["[no selection]", "Linear", "Quadratic In"])
        self.ui.comboBoxEasing.setCurrentIndex(idx)

        if t & ATConst.ITEM_MBR and t != ATConst.ITEM_GROWING_LINE:
            p = item.parent()
            self.kfCount = cnt = p.childCount()

            self.ui.labelKFCount.setText("/ {}".format(cnt - 1))
            self.ui.horizontalSlider.setMaximum(cnt - 1)

            idxTo = min(p.indexOfChild(item), cnt - 1)
            if cnt > 1:
                idxTo = max(1, idxTo)
                self.ui.horizontalSlider.setMinimum(1)

            self.ui.horizontalSlider.setValue(idxTo)
            self.currentKeyframeChanged(idxTo)

        if t in (ATConst.ITEM_GRP_MATERIAL, ATConst.ITEM_MATERIAL):

            if t == ATConst.ITEM_MATERIAL:
                self.ui.comboBoxEffect.addItem("Selected one in group", 0)

            self.ui.comboBoxEffect.addItem("Fade in", 1)
            self.ui.comboBoxEffect.addItem("Slide", 2)

            idx = self.ui.comboBoxEffect.findData(item.data(0, ATConst.DATA_EFFECT))
            if idx > 0:
                self.ui.comboBoxEffect.setCurrentIndex(idx)

        wth = []
        if not t & ATConst.ITEM_GRP and t != ATConst.ITEM_CAMERA:
            wth += [self.ui.labelName, self.ui.lineEditName]

        if t != ATConst.ITEM_OPACITY:
            wth += [self.ui.labelOpacity, self.ui.doubleSpinBoxOpacity,
                    self.ui.labelOpacity2, self.ui.doubleSpinBoxOpacity2]

        if t != ATConst.ITEM_MATERIAL:
            wth += [self.ui.labelMaterial, self.ui.comboBoxMaterial,
                    self.ui.labelMaterial2, self.ui.comboBoxMaterial2]

            if t != ATConst.ITEM_GRP_MATERIAL:
                wth += [self.ui.labelEffect, self.ui.comboBoxEffect]

        if not t & ATConst.ITEM_MBR:
            wth += [self.ui.labelDuration, self.ui.lineEditDuration,
                    self.ui.labelDelay, self.ui.lineEditDelay,
                    self.ui.labelNarration, self.ui.textEdit]

        for w in wth:
            w.setVisible(False)

        self.ui.horizontalSlider.valueChanged.connect(self.currentKeyframeChanged)
        self.ui.toolButtonPrev.clicked.connect(self.prevKeyframe)
        self.ui.toolButtonNext.clicked.connect(self.nextKeyframe)
        self.ui.pushButtonPlay.clicked.connect(self.play)
        self.ui.pushButtonPlayAll.clicked.connect(self.playAll)

    def prevKeyframe(self):
        self.ui.horizontalSlider.setValue(self.ui.horizontalSlider.value() - 1)

    def nextKeyframe(self):
        self.ui.horizontalSlider.setValue(self.ui.horizontalSlider.value() + 1)

    def currentKeyframeChanged(self, value):
        self.ui.lineEditCurrentKF.setText(str(value))
        self.ui.toolButtonPrev.setEnabled(value > 1)
        self.ui.toolButtonNext.setEnabled(value < self.kfCount - 1)

        if self.itemTo and not self.isPlaying:
            self.apply()

        idxTo = value
        if idxTo == 0:
            for w in [self.ui.labelName2, self.ui.lineEditName2, self.ui.labelDuration, self.ui.lineEditDuration,
                      self.ui.labelNarration, self.ui.textEdit]:
                w.setEnabled(False)

        idxFrom = max(0, idxTo - 1)

        p = self.item.parent()
        iFrom = p.child(idxFrom)
        iTo = p.child(idxTo)

        self.ui.comboBoxEasing.setCurrentIndex(iTo.data(0, ATConst.DATA_EASING) or 0)

        self.setupFromAndTo(iFrom, iTo)
        self.updateTime(p, idxTo)

    def setupFromAndTo(self, iFrom, iTo):
        self.itemFrom, self.itemTo = (iFrom, iTo)

        self.ui.lineEditDelay.setText(str(iFrom.data(0, ATConst.DATA_DELAY)))
        self.ui.lineEditDuration.setText(str(iTo.data(0, ATConst.DATA_DURATION)))

        nar = iTo.data(0, ATConst.DATA_NARRATION) or {}
        self.narId = nar.get("id")
        self.ui.textEdit.setPlainText(nar.get("text") or "")

        if self.type == ATConst.ITEM_CAMERA:
            self.ui.lineEditName.setText(iFrom.text(0))
            self.ui.lineEditName2.setText(iTo.text(0))

        elif self.type == ATConst.ITEM_OPACITY:
            self.ui.doubleSpinBoxOpacity.setValue(iFrom.data(0, ATConst.DATA_OPACITY) or 1)
            self.ui.doubleSpinBoxOpacity2.setValue(iTo.data(0, ATConst.DATA_OPACITY) or 1)

        elif self.type == ATConst.ITEM_MATERIAL:
            for mtl in self.layer.properties.get("materials", []):
                name, id = (mtl.get("name", ""), mtl.get("id"))
                self.ui.comboBoxMaterial.addItem(name, id)
                self.ui.comboBoxMaterial2.addItem(name, id)

            idx = self.ui.comboBoxMaterial.findData(iFrom.data(0, ATConst.DATA_MTL_ID))
            if idx > 0:
                self.ui.comboBoxMaterial.setCurrentIndex(idx)

            idx = self.ui.comboBoxMaterial2.findData(iTo.data(0, ATConst.DATA_MTL_ID))
            if idx > 0:
                self.ui.comboBoxMaterial2.setCurrentIndex(idx)

    def updateTime(self, parentItem, index):
        begin = 0
        for i in range(1, index):
            item = parentItem.child(i)
            begin += int(item.data(0, ATConst.DATA_DELAY)) + int(item.data(0, ATConst.DATA_DURATION))

        begin += int(parentItem.child(index).data(0, ATConst.DATA_DELAY))
        end = begin + int(parentItem.child(index).data(0, ATConst.DATA_DURATION))

        total = end
        for i in range(index + 1, parentItem.childCount()):
            item = parentItem.child(i)
            total += int(item.data(0, ATConst.DATA_DURATION)) + int(item.data(0, ATConst.DATA_DELAY))

        fmt = "{:.0f}:{:06.3f}"
        self.ui.labelTimeBegin.setText(fmt.format(*divmod(begin / 1000, 60)))
        self.ui.labelTimeEnd.setText(fmt.format(*divmod(end / 1000, 60)))

        self.ui.labelTotal.setText(fmt.format(*divmod(total / 1000, 60)))

    def apply(self):
        if self.type & ATConst.ITEM_MBR:
            iFrom, iTo = (self.itemFrom, self.itemTo)

            iFrom.setData(0, ATConst.DATA_DELAY, self.ui.lineEditDelay.text())
            iTo.setData(0, ATConst.DATA_DURATION, self.ui.lineEditDuration.text())
            iTo.setData(0, ATConst.DATA_EASING, self.ui.comboBoxEasing.currentIndex())

            nar = None
            text = self.ui.textEdit.toPlainText()
            if text:
                nar = {
                    "id": self.narId or ("nar_" + createUid()),
                    "text": text
                }
            iTo.setData(0, ATConst.DATA_NARRATION, nar)

            if self.type == ATConst.ITEM_CAMERA:
                iFrom.setText(0, self.ui.lineEditName.text())
                iTo.setText(0, self.ui.lineEditName2.text())

            elif self.type == ATConst.ITEM_OPACITY:
                opacity = self.ui.doubleSpinBoxOpacity.value()
                iFrom.setText(0, "Opacity '{}'".format(opacity))
                iFrom.setData(0, ATConst.DATA_OPACITY, opacity)

                opacity = self.ui.doubleSpinBoxOpacity2.value()
                iTo.setText(0, "Opacity '{}'".format(opacity))
                iTo.setData(0, ATConst.DATA_OPACITY, opacity)

            p = iTo.parent()
            self.updateTime(p, p.indexOfChild(iTo))

    def accept(self):
        #if self.type & ATConst.ITEM_GRP or self.type == ATConst.ITEM_CAMERA:
        #    self.item.setText(0, self.ui.lineEditName.text())

        if self.type & ATConst.ITEM_MBR:
            self.apply()

        if self.type in (ATConst.ITEM_GRP_MATERIAL, ATConst.ITEM_MATERIAL):
            if self.type == ATConst.ITEM_MATERIAL:
                self.item.setText(0, "Material '{}'".format(self.ui.comboBoxMaterial.currentText()))
                self.item.setData(0, ATConst.DATA_MTL_ID, self.ui.comboBoxMaterial.currentData())

            self.item.setData(0, ATConst.DATA_EFFECT, self.ui.comboBoxEffect.currentData())

        QDialog.accept(self)

    def playAnimation(self, items):
        self.panel.playAnimation(items)

        self.ui.pushButtonPlay.setText("Stop")
        self.ui.pushButtonPlayAll.setText("Stop")
        self.isPlaying = True

    def stopAnimation(self):
        self.panel.stopAnimation()
        self.isPlaying = self.isPlayingAll = False

    def play(self):
        if not self.isPlaying:
            self.apply()

            if self.type & ATConst.ITEM_MBR:
                if self.itemTo:
                    self.playAnimation([self.itemTo])
        else:
            self.stopAnimation()

    def playAll(self):
        if not self.isPlaying:
            self.apply()

            if self.type & ATConst.ITEM_MBR:
                self.playAnimation([self.item.parent()])
                self.isPlayingAll = True
        else:
            self.stopAnimation()

    # @pyqtSlot()
    def animationStopped(self):
        self.ui.pushButtonPlay.setText("Play")
        self.ui.pushButtonPlayAll.setText("Play All")

        self.isPlaying = self.isPlayingAll = False

    # @pyqtSlot(int)
    def tweenStarted(self, index):
        if self.isPlayingAll:
            if DEBUG_MODE:
                logMessage("TWEENING {} ...".format(index))
            self.ui.horizontalSlider.setValue(index + 1)