import { writable } from "svelte/store";

const createStore = () => {
  const { subscribe, set } = writable(null);
  return {
    subscribe,
    signIn: (user) => set(user),
    signOut: () => set(null),
  };
};

export const currentUser = createStore();
