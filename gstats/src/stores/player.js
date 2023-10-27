
export const usePlayerStore = defineStore('player', {
    state: () => ({
        generalStats: {},
        kdrByModule: {},
    }),
    getters: {
        generalStats: (state) => state.generalStats,
        kdrByModule: (state) => state.kdrByModule,
    },
    actions: {
        
    }
});