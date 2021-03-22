export const FEATURE_TOGGLES = {
    vipWelcome: {
      name: "feature_vip_welcome"
    }
};

export const initFeatureToggles = async () => {
    const remoteConfig = window.firebase.remoteConfig();
    await remoteConfig.fetchAndActivate();
    return remoteConfig;
};