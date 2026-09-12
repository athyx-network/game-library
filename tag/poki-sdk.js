(() => {
	const noop = () => {};
	const autoResolve = () => Promise.resolve();
	window.PokiSDK = {
		init: () => Promise.resolve(),
		initWithVideoHB: () => Promise.resolve(),
		customEvent: noop,
		commercialBreak: autoResolve,
		rewardedBreak: () => Promise.resolve(false),
		displayAd: noop,
		destroyAd: noop,
		getLeaderboard: autoResolve,
		getSharableURL: () => Promise.reject(),
		getURLParam: (n) => {
			const match = RegExp("[?&]" + n + "=([^&]*)").exec(window.location.search);
			return match ? decodeURIComponent(match[1].replace(/\+/g, " ")) : "";
		},
		gameLoadingStart: noop,
		gameLoadingFinished: noop,
		gameLoadingProgress: noop,
		gameInteractive: noop,
		roundStart: noop,
		roundEnd: noop,
		muteAd: noop,
		setDebug: noop,
		gameplayStart: noop,
		gameplayStop: noop,
		happyTime: noop,
		setPlayerAge: noop,
		togglePlayerAdvertisingConsent: noop,
		logError: noop,
		sendHighscore: noop,
		setDebugTouchOverlayController: noop,
		disableProgrammatic: noop
	};
})();