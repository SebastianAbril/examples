const Ethermon = artifacts.require('Ethermon');

contract('Ethermon should', function (/* accounts */) {

  let ethermonContract;

  before(async() => {
    ethermonContract = await Ethermon.new('NTF PET GAME', 'NFPG');
  });

  it('deploys successfully', async () => {
    const address = await ethermonContract.address;

    assert.notEqual(address, 0x0);
    assert.notEqual(address, '');
    assert.notEqual(address, null);
    assert.notEqual(address, undefined);
  });

  it('mint a new monster', async () => {
    const ANY_HP = 100;
    const ANY_ATTACK = 10;
    const ANY_DEFENSE = 5;
    const ANY_SPEED = 15;

    const result = await ethermonContract.mint(
      ANY_HP,
      ANY_ATTACK,
      ANY_DEFENSE,
      ANY_SPEED
    );

    const monsterId = result.logs[0].args.tokenId;
    const monster = await ethermonContract.getMonsterById(monsterId);

    assert.equal(monster.id, monsterId);
    assert.equal(monster.hp, ANY_HP);
    assert.equal(monster.currentHp, monster.hp);
    assert.equal(monster.attack, ANY_ATTACK);
    assert.equal(monster.defense, ANY_DEFENSE);
    assert.equal(monster.speed, ANY_SPEED);
    assert.equal(monster.level, '1');
    assert.equal(monster.pointsForSpeeding, '0');
  });

  it('train a monster', async () => {
    const monsterId = await givenAMonster();

    await ethermonContract.train(monsterId);

    const monster = await ethermonContract.getMonsterById(monsterId);

    assert.equal(monster.level, '2');
    assert.equal(monster.pointsForSpeeding, '2');
  });

  it('battle between two monster', async () => {
    const attackerId = await givenAMonster({hp: 100, attack: 10, defense: 8,speed: 15});
    const defenderId = await givenAMonster({hp: 100, attack: 10, defense: 5,speed: 5});

    await ethermonContract.battle(attackerId, defenderId);

    const attacker = await ethermonContract.getMonsterById(attackerId);
    const defender = await ethermonContract.getMonsterById(defenderId);

    assert.equal(attacker.currentHp, 94);
    assert.equal(defender.currentHp, 85);
  });

  async function givenAMonster(stats = {}) {
    const defaultStats = {
      hp: 100, 
      attack: 10, 
      defense: 5,
      speed: 15
    };

    const monsterStats = {
      ...defaultStats,
      ...stats
    };

    const result = await ethermonContract.mint(
      monsterStats.hp,
      monsterStats.attack,
      monsterStats.defense,
      monsterStats.speed
    );

    const monsterId = result.logs[0].args.tokenId;

    return monsterId;
  }
});