import Phaser from 'phaser';

export default class Bullet extends Phaser.GameObjects.Image {
	constructor({ game, key }) {
		super(game, 0, 0, key);

		this.texture.baseTexture.scaleMode = PIXI.scaleModes.NEAREST;

		this.anchor.set(0.5);
		this.checkWorldBounds = true;
		this.outOfBoundsKill = true;
		this.exists = false;

		this.tracking = false;
		this.scaleSpeed = 0;
	}

	fire({ x, y, angle, speed, gx = 0, gy = 0 }) {
		this.reset(x, y);
		this.scale.set(1);
		this.game.physics.arcade.velocityFromAngle(angle, speed, this.body.velocity);

		this.angle = angle;
		this.body.gravity.set(gx, gy);
	}

	update() {
		if(this.tracking) {
			this.rotation = Math.atan2(this.body.velocity.y, this.vody.velocity.x);
		}

		if(this.scaleSpeed > 0) {
			this.scale.x += this.scaleSpeed;
			this.scale.y += this.scaleSpeed;
		}
	}
}

export class SmallBullet extends Phaser.GameObjects.Image {
	constructor(scene) {
		super(scene, 0, 0, 'SmallBullet');
		
		this.speed = 600;
	}

	fire(x, y) {
		this.setPosition(x, y);
		this.setActive(true);
		this.setVisible(true);
	}

	update(time, delta) {
		this.x += this.speed * delta;

		if(this.x > 820)
		{
			this.setActive(false);
			this.setVisible(false);
		}
	}
}