import Phaser from 'phaser';

import background from '../assets/images/background.png';
import healthbar from '../assets/images/hud/HealthBar.png';
import health from '../assets/images/hud/HealthBarColor.png';

import powerup from '../assets/images/hud/PowerUp1.png';
import shielditem from '../assets/images/hud/shieldItem.png';

import bullet1 from '../assets/images/weapons/1.png';
import bullet2 from '../assets/images/weapons/2.png';
import bullet3 from '../assets/images/weapons/3.png';
import bullet4 from '../assets/images/weapons/4.png';
import bullet5 from '../assets/images/weapons/5.png';
import bullet6 from '../assets/images/weapons/7.png';
import bullet7 from '../assets/images/weapons/13.png';
import bullet8 from '../assets/images/weapons/10.png';
import wave1 from '../assets/images/weapons/6.png';
import wave2 from '../assets/images/weapons/9.png';
import wave3 from '../assets/images/weapons/8.png';
import megashot1 from '../assets/images/weapons/11.png';
import megashot2 from '../assets/images/weapons/12.png';
import laser from '../assets/images/weapons/14.png';
import rocket1 from '../assets/images/weapons/Rocket2.png';
import rocket2 from '../assets/images/weapons/Rocket.png';

import striker2 from '../assets/images/weapons/Striker-2.png';
import striker2big from '../assets/images/weapons/Striker-2-BIG.png';
import striker2big2 from '../assets/images/weapons/Striker-2-BIG-2.png';
import striker3big from '../assets/images/weapons/Striker-3-BIG.png';
import striker3big2 from '../assets/images/weapons/Striker-3-BIG-2.png';
import striker6big from '../assets/images/weapons/Striker-6-BIG.png';
import striker6big2 from '../assets/images/weapons/Striker-6-BIG-2.png';
import striker7big from '../assets/images/weapons/Striker-7-BIG.png';
import striker7big2 from '../assets/images/weapons/Striker-7-BIG-2.png';
import striker7big3 from '../assets/images/weapons/Striker-7-BIG-3.png';
import striker7big4 from '../assets/images/weapons/Striker-7-BIG-4.png';
import striker7big5 from '../assets/images/weapons/Striker-7-BIG-5.png';
import striker8big from '../assets/images/weapons/Striker-8-BIG-2.png';
import striker8big2 from '../assets/images/weapons/Striker-8-BIG-2.png';
import striker10big from '../assets/images/weapons/Striker-10-BIG.png';

import ship1 from '../assets/images/ships/2.png';
import ship2 from '../assets/images/ships/6b.png';
import ship3 from '../assets/images/ships/3.png';
import ship4 from '../assets/images/ships/4.png';

import enemy1 from '../assets/images/enemies/10.png';
import enemy2 from '../assets/images/enemies/jelly.png';
import enemy3 from '../assets/images/enemies/jelly-2.png';
import enemy4 from '../assets/images/enemies/11.png';
import enemy5 from '../assets/images/enemies/9.png';
import boss1 from '../assets/images/enemies/1.png';
import boss2 from '../assets/images/enemies/7.png';
import boss3 from '../assets/images/enemies/8.png';

export default class Preloader extends Phaser.Scene {
	get score() { return this._score; }
	set score(value) { this._score = value; this.registry.set('score', value); }

	get lives() { return this._lives; }
	set lives(value) { this._lives = value; this.registry.set('lives', value); }

	constructor() {
		super({
			key: 'preloader'
		});

		this._score = 0;
		this._lives = 5;
	}

	preload() {
		// Load in images and sprites
		this.preloadHud();
		this.preloadWeapons();
		this.preloadExplosions();
		this.preloadPlayerShips();
		this.preloadEnemies();
		this.preloadSounds();
	}

	preloadSounds() {
		this.load.audio('level1theme', ['/assets/sounds/1.ogg']);
		this.load.audio('level2theme', ['/assets/sounds/2.ogg']);
		
		this.load.audio('shoot1', ['/assets/sounds/shoot1.wav']);
		this.load.audio('shoot2', ['/assets/sounds/shoot2.wav']);
		this.load.audio('shoot3', ['/assets/sounds/shoot3.wav']);
		this.load.audio('shoot4', ['/assets/sounds/shoot4.wav']);
		this.load.audio('shoot5', ['/assets/sounds/shoot5.wav']);
		this.load.audio('shoot6', ['/assets/sounds/shoot6.wav']);
		this.load.audio('shoot7', ['/assets/sounds/shoot7.wav']);
		this.load.audio('laser', ['/assets/sounds/Laser.wav']);

		this.load.audio('shoot-destroy-1', ['/assets/sounds/shoot-destroy-1.wav']);
		this.load.audio('shoot-destroy-2', ['/assets/sounds/shoot-destroy-2.wav']);
		this.load.audio('shoot-destroy-3', ['/assets/sounds/shoot-destroy-3.wav']);

		this.load.audio('alert', ['/assets/sounds/alert.wav']);
		this.load.audio('death', ['/assets/sounds/Death.wav']);
		this.load.audio('playerHit', ['/assets/sounds/playerHit.wav']);

		this.load.audio('bossShoot', ['/assets/sounds/bossShoot.wav']);
		this.load.audio('bossDeath', ['/assets/sounds/bossDeath.wav']);
		this.load.audio('darkShoot', ['/assets/sounds/darkShoot.wav']);
	}

	preloadEnemies() {
		this.load.image('enemy1', '/assets/images/enemies/10.png');
		this.load.image('enemy2', '/assets/images/enemies/jelly.png');
		this.load.image('enemy3', '/assets/images/enemies/jelly-2.png');
		this.load.image('enemy4', '/assets/images/enemies/11.png');
		this.load.image('enemy5', '/assets/images/enemies/9.png');
		this.load.image('boss1', '/assets/images/enemies/1.png');
		this.load.image('boss2', '/assets/images/enemies/7.png');
		this.load.image('boss3', '/assets/images/enemies/8.png');
	}

	preloadPlayerShips() {
		this.load.image('ship1', '/assets/images/ships/2.png');
		this.load.image('ship2', '/assets/images/ships/6b.png');
		this.load.image('ship3', '/assets/images/ships/3.png');
		this.load.image('ship4', '/assets/images/ships/4.png');
	}

	preloadExplosions() {
		this.load.image('striker2', '/assets/images/weapons/Striker-2.png');
		this.load.image('striker2big', '/assets/images/weapons/Striker-2-BIG.png');
		this.load.image('striker2big2', '/assets/images/weapons/Striker-2-BIG-2.png');
		this.load.image('striker3big', '/assets/images/weapons/Striker-3-BIG.png');
		this.load.image('striker3big2', '/assets/images/weapons/Striker-3-BIG-2.png');
		this.load.image('striker6big', '/assets/images/weapons/Striker-6-BIG.png');
		this.load.image('striker6big2', '/assets/images/weapons/Striker-6-BIG-2.png');
		this.load.image('striker7big', '/assets/images/weapons/Striker-7-BIG.png');
		this.load.image('striker7big2', '/assets/images/weapons/Striker-7-BIG-2.png');
		this.load.image('striker7big3', '/assets/images/weapons/Striker-7-BIG-3.png');
		this.load.image('striker7big4', '/assets/images/weapons/Striker-7-BIG-4.png');
		this.load.image('striker7big5', '/assets/images/weapons/Striker-7-BIG-5.png');
		this.load.image('striker8big', '/assets/images/weapons/Striker-8-BIG-2.png');
		this.load.image('striker8big2', '/assets/images/weapons/Striker-8-BIG-2.png');
		this.load.image('striker10big', '/assets/images/weapons/Striker-10-BIG.png');
	}

	preloadHud() {
		this.load.image('background', '/assets/images/background.png');
		this.load.image('healthbar', '/assets/images/hud/HealthBar.png');
		this.load.image('health', '/assets/images/hud/HealthBarColor.png');
		this.load.image('powerup', '/assets/images/hud/PowerUp1.png');
		this.load.image('shielditem', '/assets/images/hud/shieldItem.png');
	}

	preloadWeapons() {
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
	}

	create() {
		this.registry.set('score', this.score);
		this.registry.set('lives', this.lives);
		this.registry.events.on('changeData', this.updateData, this);

		this.scene.start('level1');
	}

	updateData(parent, key, value) {
		if(key === 'score') {
			this.score = value;
		}
		else if(key === 'lives') {
			this.lives = value;
		}
	}
}