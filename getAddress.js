const ethers = require("ethers")
const axios = require("axios")

const STRATEGIES_ENDPOINT = 'https://lockers.stakedao.org/api/strategies/cache';
const LOCKERS_ENDPOINT = 'https://lockers.stakedao.org/api/lockers/cache';

const getAddress = async () => {
    const resp = await Promise.all([
        axios.get(`${STRATEGIES_ENDPOINT}/angle`),
        axios.get(`${STRATEGIES_ENDPOINT}/curve`),
        axios.get(`${STRATEGIES_ENDPOINT}/balancer`),
        axios.get(`${LOCKERS_ENDPOINT}`)
      ]);
      const angleStrategies = resp[0].data;
      const curveStrategies = resp[1].data;
      const balancerStrategies = resp[2].data;
      const lockers = resp[3].data;

      const strats = angleStrategies
        .concat(curveStrategies)
        .concat(balancerStrategies)
        .concat(lockers);

    
      const lg = []
      const len = Object.keys(strats).length;
      for (let i = 0; i < len; ++i){
        lg.push(ethers.utils.getAddress(strats[i].infos.sdtLiquidityGauge || strats[i].infos.gauge));
      }
      console.log("Addresses : ", lg);
}

getAddress();

