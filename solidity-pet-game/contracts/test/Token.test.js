const Token = artifacts.require('Token');

contract('Token should', function (/* accounts */) {

  let tokenContract;

  before(async() => {
    tokenContract = await Token.new('NTF PET GAME', 'NFPG');
  });

  it('deploys successfully', async () => {
    const address = await tokenContract.address;

    assert.notEqual(address, 0x0);
    assert.notEqual(address, '');
    assert.notEqual(address, null);
    assert.notEqual(address, undefined);
  });

  it('mint a new Pet', async () => {
    const ANY_DAMAGE = 100;
    const ANY_MAGIC = 200;
    const ANY_ENDURANCE = 100;

    await tokenContract.mint(ANY_DAMAGE, ANY_MAGIC, ANY_ENDURANCE);

    const pet = await tokenContract.getTokenDetails(0);

    assert.equal(pet.damage, ANY_DAMAGE);
    assert.equal(pet.magic, ANY_MAGIC);
    assert.equal(pet.endurance, ANY_ENDURANCE);
    assert.notEqual(pet.lastMeal, null);
    assert.notEqual(pet.lastMeal, undefined);
  });

  it('feed a Pet', async () => {
    const PET_ID = 0;
    const ANY_DAMAGE = 100;
    const ANY_MAGIC = 200;
    const ANY_ENDURANCE = 100;

    await tokenContract.mint(ANY_DAMAGE, ANY_MAGIC, ANY_ENDURANCE);

    const beforeFeedPet = await tokenContract.getTokenDetails(PET_ID);

    await tokenContract.feed(PET_ID);

    const afterFeedPet = await tokenContract.getTokenDetails(PET_ID);

    assert.notEqual(beforeFeedPet.lastMeal, afterFeedPet.lastMeal);
  });


});