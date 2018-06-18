import Phaser from 'phaser';

export class SimpleEnemy extends Phaser.GameObjects.Image {
	constructor(scene) {
		super(scene, 0, 0, 'enemy1');

		this.direction = 'left';
	}

	update(time, delta) {
		if(this.y < 0) {
			this.setActive(false);
			this.setVisible(false);
			return;
		}

		this.y += 1;
	}
}

export class StrafingEnemy extends Phaser.GameObjects.Image {
	get movementSpeed() { return 2; }
	
	constructor(scene) {
		super(scene, 0, 0, 'enemy2');
	}

	update(time, delta) {
		if(this.y > 800) {
			this.setActive(false);
			this.setVisible(false);
			return;
		}

		if(this.direction === 'left')
			this.x -= this.movementSpeed;
		else
			this.x += this.movementSpeed;

		this.y += 1;

		if(this.x <= 0) {
			this.direction = 'right';
			this.x = 0;
		}
		else if(this.x >= this.scene.cache.game.config.width) {
			this.direction = 'left';
			this.x = this.scene.cache.game.config.width;
		}
	}
}

export class ZigZagEnemy extends Phaser.GameObjects.Image {
	constructor(scene) {
		super(scene, 0, 0, 'enemy3');

		this.setScale(Phaser.Math.Between(1, 2));
		this.path = Phaser.Curves.Path(100, -50);
		this.path.lineTo(100, 50);

		const max = 6;
		var h = 500 / max;
		
		for(let i = 0; i < max; ++i) {
			if(i % 2 === 0)
				this.path.lineTo(700, 50 + h * (i + 1));
			else
				this.path.lineTo(100, 50 + h * (i + 1));
		}

		this.path.lineTo(100, 950);

		this.setData('vector', new Phaser.Math.Vector2());
		// this.tweens.add({
		// 	targets: this,
		// 	t: 1,
		// 	ease: 'linear',
		// 	duration: 5000,
		// 	repeat: -1
		// })
	}

	update() {
		var t = this.z;
		var vec = this.getData('vector');

		this.path.getPoint(t, vec);

		this.setPosition(vec.x, vec.y);
		this.setDepth(this.y);
	}
}

export class CurveEnemy extends Phaser.GameObjects.Image {
	constructor(scene) {
		super(scene, 0, 0, 'enemy4');

		this.setScale(Phaser.Math.Between(1, 2));
		this.setData('vector', new Phaser.Math.Vector2());

		this.path = new Phaser.Curves.Path(0, 0);

		// cubicBezierTo: function (x, y, control1X, control1Y, control2X, control2Y)
		this.path.cubicBezierTo(500, 100, 75, 150, 100, 100);
		this.path.cubicBezierTo(200, 320, 700, 500, 550, 250);
		this.path.cubicBezierTo(200, 500, -50, 400, -50, 500);
		this.path.cubicBezierTo(800, 650, 700, 550, 650, 600);

		// this.tweens.add({
		// 	targets: this,
		// 	t: 1,
		// 	ease: 'linear',
		// 	duration: 5000,
		// 	repeat: -1
		// });
	}

	update() {
		const vector = this.getData('vector');

		this.path.getPoint(this.z, vector);
		this.setPosition(vector.x, vector.y);
		this.setDepth(this.y);
	}
}