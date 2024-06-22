function initCordovaApp() {
	// window.onload = function(){ 
	document.addEventListener("deviceready", function () {
		var permissions = cordova.plugins.permissions;
		listPermissions = [
			permissions.CAMERA,
			permissions.ACCESS_COARSE_LOCATION,
			permissions.ACCESS_FINE_LOCATION,
			permissions.ACCESS_LOCATION_EXTRA_COMMANDS
		];

		permissions.hasPermission(listPermissions, function (status) {
			if (!status.hasPermission) {
				function error() {
					navigator.notification.alert('Camera permission is not turned on');
				}

				function success(status) {
					if (!status.hasPermission) error();
				}
				
				permissions.requestPermissions(listPermissions, success, error);
			}
		});


		// if (device && device.platform && device.platform == "Android") {
		// 	// alert("androin");
		// 	navigator.notification.alert("Android");
		// 	// alert("Android");
		// } else {
		// 	// alert("not androin");
		// 	navigator.notification.alert("not Android");
		// 	// alert("not Android");
		// }
	}, false);
	// }
}