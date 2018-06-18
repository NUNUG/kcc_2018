import Phaser from 'phaser';
import Preloader from './scenes/preloader';
import Level1 from './scenes/level1';

const config = {
	type: Phaser.AUTO,
	width: 800,
	height: 600,
	physics: {
		default: 'arcade',
		arcade: {}
	},
	scene: [
		Preloader,
		Level1
	]
};

const game = new Phaser.Game(config);