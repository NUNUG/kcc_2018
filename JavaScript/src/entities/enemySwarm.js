import Phaser from 'phaser';
import Enemy from './enemy';

export default class EnemySwarm extends Phaser.Group {
	constructor({ scene, size = 10, name = 'enemy1', enemyNames }) {
		super(scene, scene.world, 'Enemy Swarm', false, true, Phaser.Physics.Arcade);

		if(!enemyNames) {
			enemyNames = {
				[name]: size
			};
		}

		Object.entries(enemyNames).forEach(([name, size]) => {
			for(let i = 0; i < size; ++i) {
				const enemy = new Enemy({ scene, key: name });
				this.add(enemy, true);
			}
		});
	}

	spawn() {

	}
}