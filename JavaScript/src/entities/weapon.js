import Phaser from 'phaser';
import { SmallBullet } from './bullet';

export class SingleSmallBullet extends Phaser.Group {
	get bulletSpeed() { return 600; }
	get fireRate() { return 100; }
	
	constructor(scene) {
		super(scene, scene.world, 'Single Small Bullet', false, true, Phaser.Physics.Arcade);
		this.classType = SmallBullet;
		
		this.createMultiple({
			active: false,
			key: 'SmallBullet',
			repeat: 40
		});

		this.lastFire = 0;
	}

	fire(source) {
		if(this.time.now < this.lastFire + this.fireRate)
			return;

		const x = source.x + 10;
		const y = source.y + 10;

		const bullet = this.get();
		if(bullet) {
			bullet.fire({ x, y, angle: 0, speed: this.bulletSpeed });
			this.lastFire = this.time.now;
		}
	}
}