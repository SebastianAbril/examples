const Migrations = artifacts.require("Ethermon");

module.exports = function (deployer) {
  deployer.deploy(Migrations, 'NTF PET GAME', 'NFPG');
};
