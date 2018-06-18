import Phaser from 'phaser';
import background from './assets/images/background.png';
import healthbar from './assets/images/hud/HealthBar.png';
import health from './assets/images/hud/HealthBarColor.png';
import powerup from './assets/images/hud/PowerUp1.png';
import shielditem from './assets/images/hud/shieldItem.png';
import bullet1 from './assets/images/weapons/1.png';
import bullet2 from './assets/images/weapons/2.png';
import bullet3 from './assets/images/weapons/3.png';
import bullet4 from './assets/images/weapons/4.png';
import bullet5 from './assets/images/weapons/5.png';
import bullet6 from './assets/images/weapons/7.png';
import bullet7 from './assets/images/weapons/13.png';
import bullet8 from './assets/images/weapons/10.png';
import wave1 from './assets/images/weapons/6.png';
import wave2 from './assets/images/weapons/9.png';
import wave3 from './assets/images/weapons/8.png';
import megashot1 from './assets/images/weapons/11.png';
import megashot2 from './assets/images/weapons/12.png';
import laser from './assets/images/weapons/14.png';
import rocket1 from './assets/images/weapons/Rocket2.png';
import rocket2 from './assets/images/weapons/Rocket.png';
import ship1 from './assets/images/ships/2.png';
import ship2 from './assets/images/ships/6b.png';
import ship3 from './assets/images/ships/3.png';
import ship4 from './assets/images/ships/4.png';
import enemy1 from './assets/images/enemies/10.png';
import enemy2 from './assets/images/enemies/jelly.png';
import enemy3 from './assets/images/enemies/jelly-2.png';
import enemy4 from './assets/images/enemies/11.png';
import enemy5 from './assets/images/enemies/9.png';
import boss1 from './assets/images/enemies/1.png';
import boss2 from './assets/images/enemies/7.png';
import boss3 from './assets/images/enemies/8.png';

export default {
	type: Phaser.AUTO,
	width: 800,
	height: 600,
	physics: {
		default: 'arcade',
		arcade: {}
	},
	scene: {
		preload,
		create,
		update,
		extend: {
			player: null
		}
	}
};

function preload() {
	// Load in images and sprites
	this.load.image('background', '/assets/images/background.png');
	this.load.image('healthbar', '/assets/images/hud/HealthBar.png');
	this.load.image('health', '/assets/images/hud/HealthBarColor.png');
	this.load.image('powerup', '/assets/images/hud/PowerUp1.png');
	this.load.image('shielditem', '/assets/images/hud/shieldItem.png');

	this.load.image('bullet1', '/assets/images/weapons/1.png');
	this.load.image('bullet2', '/assets/images/weapons/2.png');
	this.load.image('bullet3', '/assets/images/weapons/3.png');
	this.load.image('bullet4', '/assets/images/weapons/4.png');
	this.load.image('bullet5', '/assets/images/weapons/5.png');
	this.load.image('bullet6', '/assets/images/weapons/7.png');
	this.load.image('bullet7', '/assets/images/weapons/13.png');
	this.load.image('bullet8', '/assets/images/weapons/10.png');
	this.load.image('wave1', '/assets/images/weapons/6.png');
	this.load.image('wave2', '/assets/images/weapons/9.png');
	this.load.image('wave3', '/assets/images/weapons/8.png');
	this.load.image('megashot1', '/assets/images/weapons/11.png');
	this.load.image('megashot2', '/assets/images/weapons/12.png');
	this.load.image('laser', '/assets/images/weapons/14.png');
	this.load.image('rocket1', '/assets/images/weapons/Rocket2.png');
	this.load.image('rocket2', '/assets/images/weapons/Rocket.png');
	
	this.load.image('ship1', '/assets/images/ships/2.png');
	this.load.image('ship2', '/assets/images/ships/6b.png');
	this.load.image('ship3', '/assets/images/ships/3.png');
	this.load.image('ship4', '/assets/images/ships/4.png');

	this.load.image('enemy1', '/assets/images/enemies/10.png');
	this.load.image('enemy2', '/assets/images/enemies/jelly.png');
	this.load.image('enemy3', '/assets/images/enemies/jelly-2.png');
	this.load.image('enemy4', '/assets/images/enemies/11.png');
	this.load.image('enemy5', '/assets/images/enemies/9.png');
	this.load.image('boss1', '/assets/images/enemies/1.png');
	this.load.image('boss2', '/assets/images/enemies/7.png');
	this.load.image('boss3', '/assets/images/enemies/8.png');

	// this.load.bitmapFont('textfont', '/assets/Font20x20.png', '/assets/Font20x20.xml');
	// this.load.bitmapFont('gamefont', '/assets/Font46x37.png', '/assets/Font46x37.xml');

	// this.load.sound('')
}

function create() {
	// Create world bounds
	const backgroundImage = this.add.tileSprite(0, 0, 1280, 720, 'background');
	// this.physics.setBoundsToWorld();

	this.player = this.add.sprite(38, 34, 'ship1');
	this.physics.arcade.enable(player);
	this.player.body.collideWorldBounds = true;
	this.player.health = 10;
}

function update() {
	// update the objects
}
