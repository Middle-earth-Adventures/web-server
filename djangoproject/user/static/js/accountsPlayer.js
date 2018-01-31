var playersList = new Vue({
	el: '#playersRow',
	data: {
		playersList: []
	},
	mounted : function() {
		this.getPlayersList()
	},
	methods: {
		getPlayersList: function() {
			console.log("Calling getPlayersList");
			this.$http.get('player/accountsPlayers').then(response => {
                this.playersList = response.body.players;
                console.log("Players: " + response.body.players);
            }, response => {
                this.playersList = [];
                console-log("No hay jugadores en esta cuenta");
			});
		}
	}
});
