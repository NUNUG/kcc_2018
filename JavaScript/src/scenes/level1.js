import Phaser, { Scene } from 'phaser';
import { SimpleEnemy, StrafingEnemy } from '../entities/enemy';
// import EnemySwarm from '../entities/enemySwarm';

export default class Level1 extends Scene {
	get level1SpawnRate() { return 5000; }
	get level2SpawnRate() { return 15000; }
	get movementSpeed() { return 3; }
	
	constructor() {
		super({
			key: 'level1',
			physics: {
				default: 'arcade',
				arcade: {
					debug: true
				}
			}
		});

		this.staticBackground = null;
		this.scrollingBackground = null;
		this.player = null;
		this.level1Enemies = null;
		this.boss = null;
		this.level2Enemies = null;
		this.particles = null;
		this.emitter = null;

		this.cursors = null;
		this.game = null;

		this.level1EnemyCount = 50;
		this.level2EnemyCount = 25;

		this.lastLevel1Spawn = 0;
		this.lastLevel2Spawn = 50;

		this.sounds = {
			theme: null,
			playerHit: null
		};
	}

	create() {
		this.game = this.scene.get('preloader');
		
		this.staticBackground = this.add.image(0, 0, 'background');
		this.staticBackground.setTint(0x333333);
		this.staticBackground.setOrigin(0.5);

		this.sound.pauseOnBlur = true;
		
		this.level1Enemies = this.physics.add.group({
			classType: SimpleEnemy,
			maxSize: this.level1EnemyCount,
			runChildUpdate: true,
			frameQuantity: this.level1EnemyCount
		});
		this.level2Enemies = this.physics.add.group({
			classType: StrafingEnemy,
			maxSize: this.level2EnemyCount,
			runChildUpdate: true,
			frameQuantity: this.level2EnemyCount
		});

		const level1Spawn = () => {
			this.spawnEnemy(this.level1Enemies, true);
			this.level1EnemyCount--;
			if(this.level1EnemyCount > 0) {
				const max = this.level1SpawnRate * (this.level1EnemyCount / 50);
				this.time.addEvent({
					delay: Phaser.Math.Between(500, max + 500),
					loop: false,
					callback: level1Spawn
				});
			}
		};
		const level2Spawn = () => {
			this.spawnEnemy(this.level2Enemies, true);
			this.level2EnemyCount--;
			if(this.level2EnemyCount > 0) {
				const max = this.level2SpawnRate * (this.level2EnemyCount / 50);
				this.time.addEvent({
					delay: Phaser.Math.Between(1000, max + 1000),
					loop: false,
					callback: level2Spawn
				});
			}
		};

		this.time.addEvent({
			delay: this.level1SpawnRate,
			loop: false,
			callback: level1Spawn
		});
		this.time.addEvent({
			delay: this.level2SpawnRate,
			loop: false,
			callback: level2Spawn
		});

		this.particles = this.add.particles('striker2');
		this.emitter = this.particles.createEmitter({
			angle: { min: 0, max: 360 },
			speed: { min: 50, max: 200 },
			quantity: { min: 40, max: 50 },
			lifespan: { min: 200, max: 500 },
			alpha: { start: 1, end: 0},
			scale: { min: 0.5, max: 0.5 },
			rotate: { start: 0, end: 360 },
			gravity: 800,
			on: false
		});

		this.player = this.physics.add.image(400, 550, 'ship1');
		this.player.setDrag(0.99);
		this.player.setMaxVelocity(400);
		this.player.setActive(true).setVisible(true);
		this.player.setCollideWorldBounds(true);

		this.physics.add.overlap(this.player, this.level1Enemies, this.playerCollideWithEnemy, this.playerCollideWithEnemy, this);
		this.physics.add.overlap(this.player, this.level2Enemies, this.playerCollideWithEnemy, this.playerCollideWithEnemy, this);

		this.cursors = this.cache.game.input.keyboard.createCursorKeys();

		this.sounds.theme = this.sound.add('level1theme');
		this.sounds.theme.loop = true;
		this.sounds.theme.volume = 0.2;
		this.sounds.theme.play();
		this.sounds.playerHit = this.sound.add('playerHit');
		this.sounds.playerHit.loop = false;
		this.sounds.playerHit.volume = 0.5;

		this.registry.events.on('changedata', this.updateData, this);
	}

	update() {
		this.staticBackground.tilePositionY -= 1;
		
		this.updateEnemies();

		this.updatePlayer();

		// Once the boss is killed, here's how you change scenes:
		// this.scene.start('level2');
	}

	updateEnemies() {

	}

	updatePlayer() {
		this.player.setAcceleration(0);

		if(this.cursors.left.isDown) {
			 this.player.setAccelerationX(-300);
		}
		else if(this.cursors.right.isDown) {
			this.player.setAccelerationX(300);
		}
		if(this.cursors.up.isDown) {
			this.player.setAccelerationY(-100);
		}
		else if(this.cursors.down.isDown) {
			this.player.setAccelerationY(400);
		}

		// Uncomment this section and comment out the above section for easier controls
		// this.player.setVelocity(0);

		// if(this.cursors.left.isDown) {
		// 	this.player.setVelocityX(-300);
		// }
		// else if(this.cursors.right.isDown) {
		// 	this.player.setVelocityX(300);
		// }
		// if(this.cursors.up.isDown) {
		// 	this.player.setVelocityY(-200);
		// }
		// else if(this.cursors.down.isDown) {
		// 	this.player.setVelocityY(400);
		// }
	}

	spawnEnemy(group, randomX = false) {
		const enemy = group.get();
		
		if(!enemy)
			return;

		let x = 0;
		if(randomX)
			x = Phaser.Math.Between(20, this.cache.game.config.width - 20);
		
		enemy.x = x;
		enemy.y = 0;
		
		enemy.setActive(true)
		.setVisible(true)
		.setScale(Phaser.Math.Between(1, 2));
	}

	playerCollidedWithBullet (player, bullet) {
		bullet.destroy();
		this.cameras.main.shake(100, 0.01, 0.01);

		// TODO: Subtract a life from player and check if game over
	}

	playerCollideWithEnemy (player, enemy) {
		if(!this.player.invincible) {
			this.cameras.main.shake(100, 0.01, 0.01);
			this.sounds.playerHit.play();
			this.player.invincible = true;
			this.time.addEvent({
				delay: 1500,
				loop: false,
				callback: () => { this.player.invincible = false; }
			})
		}
	}

	updateData(parent, key, value) {
		
	}
}