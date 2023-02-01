import json 
from datetime import datetime

# List of addresses
addresses = [
        # Curve
        "0xC891a1BaCF802127874054e703b386346fE94b00",
        "0x531167aBE95375Ec212f2b5417EF05a9953410C1",
        "0x1E3923A498de30ff8C5Ac8bfAb1De9AFa58fDE5d",
        "0xf99FD99711671268EE557fEd651EA45e34B2414f",
        "0x4D69ad5F243571AA9628bd88ebfFA2C913427b0b",
        "0xfA51194E8eafc40523574A65C1e4606E1432408B",
        "0xaC7606876CeC9C02dC2dFe057F4024165D7cd86F",
        "0x087143dDEc7e00028AA0e446f486eAB8071b1f53",
        "0xba621b27F071E249713866d7D7D0A97B12D2fa9b",
        "0xa5342c2Cc0cA11B5923FDbcFa194CE55e77E0a53",
        "0xfe96Ceb1616c609d7ECdD15aB030b120831e6209",
        "0x6E9E36db9bf5c5867D774f47da36DA568ce43327",
        "0x28766020a5A8D3325863Bf533459130DDb0c3657",
        "0xe2867CeDeBB7F8eA60f52c9B1e8A216Adbb2F2ab",
        "0x822Faec5aa8fA750C73F8247977FFC78314d0B8c",
        "0x62EAa306DB32B5bE5d91cfdc1f87984EDac24059",
        "0xA89B9c336764c9Ae5f64Bc19688601341974bc22",
        "0x8527b2201Df6bfd09855AE5b28475DcC4A33C4f8",
        "0xd382e1D8045f45264e4A661eDA8Efb9396A58a79",
        "0x8fAC850769B6bbeEe28ae9B987C19e04999aA439",
        "0x96B5de061f4733E967E1B25569C77f5D034CAD13",
        "0xAF2E13cC54E0691A65D09cF625DD10913E5D9A4C",
        "0x8C8c4bbA402A1E037075ED437BAC4c487230016b",
        "0x9B85d6e87350c021616Ae3DA78b9B1335c68283A",
        "0x0F351Da018B93538F52E7120a8Cd2B4339a8013F",
        "0xb10DE77F94AFd8080FB7b563ee0d6388291F07Fb",
        "0xA7Ae691A17CA71Ca24b2D21De117213c2b64A54b",
        "0xBe77585F4159e674767Acf91284160E8C09b96D8",
        "0x78f4f7025D5DD8ad754f21b23Ee1C0B77c371767",
        "0x5056c3f17e45bdF11e09b1EF82a949dD68159C0E",
        "0x520D7399c82958cB9F96828B40E0AD55F76D9EbF",
        "0x3B51fC10715D4208cAF4291849f50bF442B8C3Cb",
        "0xd730d12CDCE7B7bBae1980bf1f9D3451049F766B",
        "0x8c2dA60858FB7003F94edbB97ac50aB880b40Ba7",
        "0x7866d0FcfEf177F8Af857F22be9e4246F4fceC65",
        "0x1dF8f590812F92769E677DcBE79CE54f19A58732",
        "0xfA2a590f0bF2227A18f02124e7EF91256F952688",
        "0x704547A51395cC72332C6F83dF41D795755CFa1A",
        "0xAf7315BD7Fe6e6950b217F185FDA60Ea1f72412A",
        "0xa81920e413ad03Bc2DE9B1eF6D024fb3e2C21E7B",
        "0x951a88f0F88996b8Cde4403164182b8Fc148Bd4B",
        "0xc0F082C886b94f36F67C6659bE01C0069968Cd0E",
        "0x3794C7C69B9c761ede266A9e8B8bb0f6cdf4E3E5",
        "0xBb54780a563686940057fEde5472F03089363d7c",
        "0x91F63E26dB25328Ad451681CFf568f9024347340",
        "0x8C52985e1E23B81a30c163BC3477ff8453494c22",
        "0x6Fb81473F546457a96E1A5475a1f0A1717C18873",
        "0x4c43cAecB45496FA7A8f874813F86F1D873a6e8F",
        "0x359EB1f29f22191bC5723050Be2feA02Cd9ba81e",
        "0x6b578A102fb2899b2cfF2E4c5857F428d6353ce6",
        "0x1B31C86024145583Ff37024A6B9aa8581A5070De",
        "0x4a1C13D3887AE6e7289c4e0Cd7Ed1a4d1A3e21AE",
        "0xc9CB5e84ADFa9F32Ed183e15ef423Bce93B845a9",
        "0xCE85de920110af9101f77620E901743c16b58FDd",
        "0x8672E5C9E724E593afF47549E3D47EEB9B750aB3",
        "0x63f222079608EEc2DDC7a9acdCD9344a21428Ce7",
        "0xF05c0614448EAB9EB2cB93B31Db8Ab54E4C8b9dB",
        "0x971662e2106582582859149241c1FcfDE8D5DBf7",
        "0x0aa086A48Fbe6D97D315e2a6B0Db3d526d4C63E5",
        "0x5Be7285Fb9A355e1bA97546B1178Fe2c40118DF7",
        "0x227eB2769f5Cd06AB590532Ec03E4b69dA0FdD8f",
        "0x54aA01Ed2a0533CD9E58799C0b32AC7e1554C4cf",
        "0x8474ed9bAe897B476aA98b7f1595a93e5E4A99cD",
        "0xf6fb52B2624aD7d37e219e8c3503c248ec6d8C52",
        "0xDE1F1698cD6228892fEAD129b733100367564c40",
        "0xA865a9C7d30C91658e3630b501E74F712b329c78",
        "0x4F3a2Ad919471ab67104f2e0a17D820096d9Be2A",
        "0x6931Dab8E59146f9cdD72e5549A6e09Cd491C6d6",
        "0xcBA53d97121Cc23E1506507a444cB42066bc0dC2",
        "0xA4eeEB03e66E6BF5E37BEbA946754944C024DcDb",
        "0x1aA62A793423d49496078F6814320706d91094AC",
        "0x1c963C8d7ABbB0f3521510a849349135c61Da9A1",
        "0xB3a33E69582623F650e54Cc1cf4e439473A28D26",
        "0x4b95F9f85857341cC2876c15C88091a04eE5Cb31",
        "0x131Dc928F9Dad07F43CEfF269e1674b7eBbFcBB1",
        "0x31539d93f3504571A5ec85510ae15289A3b299De",
        "0x6C43E4cf922D5448E4ee73f7267FE8e294740811",
        "0xc4649B184dBd1A4448c4d529fFbD1AD130289678",
        "0x5DA19B47CF94cbC859605c5525539BaB4844C74F",
        "0x2E2E5655A07f750a28d2c1DB492c4F67E20F6630",
        "0x2472f84B42a2a80003DF5d3EA03Aa40A45ae0BE8",
        "0x46A3c9048204431eAc65433fC311c2BAe583494E",
        "0x4514564B00A007b93d0eBF455f7322254fCD5b93",
        "0xE0d086E44bd5BB88d3F381440D5345C1f2dcDaCa",
        # Angle
        "0xAC9978DB68E11EbB9Ffdb65F31053A69522B6320",
        "0xaF32c61C4a2F79b16D8D1D36455196115F454A9b",
        "0xB6261Be83EA2D58d8dd4a73f3F1A353fa1044Ef7",
        "0x6492891C4b0d69D057Bb3707C54A62CF0878E05e",
        "0x125FC0b592Db2a21fea8a5f6B2F86b1D6417Bf66",
        "0x61542F1086ddADa25661ca0A7f2f801d76499136",
        # Balancer
        "0x153E7FBC27161B6CC87fb3DaA77D65d4FDFA11B5",
        "0x33807ECb10374f45f548F62261Bb2ABd05915E00",
        "0xd3FAE73C65baBcEb942D30EBD2c3fD766602491d",
        "0x1Aff1BEeB36b2A8212D27Cc95DcEaA7ec917cfb4",
        "0x15f562Bb33FC265204bea2da4Fc15811Ac187002",
        "0x2721959Fb02EAD308d0880Eef7356fE4B110547E",
        "0x3Df61C8599D10410Fa0040A6FDbD7C2D6339386d",
        "0xd75Da4f453aa61787FabaFBce666293E529FB80A",
        "0xe0aD59959C8baf06799af5E875586e928D5f4465",
        "0xB7511a339Efd3014502A7Fb4F74cec15cE2e3895",
        "0xfE0A20683294851a1722eA097ae013040821e144",
        "0xeE622c9a63926D8efDC9eD24409090a6A1f24489",
        "0x7daF16880D24618045554B63a020Fe10bf4EDB42",
        "0xA35F8a6712f76661Ef5435576f8288c5A3abf654",
        "0x6738CBD4eE105C5Fd45D244c14d80708A7460baA",
        "0x3481740e8F92D237dd01B7b9c0FdCb43Cb0359ac",
        "0xfB1bfa535D1409726F97AcDd790Bd75d05DC85A8",
        "0x0914cE39D5043de294e9149fb958e75B31D50f2a",
        "0xE1401a11348461462e731fE242146EE890747F5e",
        "0x69a69D982bABc508C1763c9F9Bb984723da004C1",
        "0x76fB1951F3395031B3ec703a16567ab92E792770",
        "0xd9Db9e29D64F025Ea8d4140836Fe86fF977A479A",
        "0x85A23DB89CFCBa2748777Aa709DD46d667c548e6",
        "0xc151B121a6654AB86Bf9Ec311b5aA7f585c7AB5D",
        "0x7Fcab1C0168de68f0c19b72ba49Ba1a9798D21C3",
        "0x5bf40874B125c3814a8a38Ef72f34D087bA85d04",
        "0x6c7FBcAADBC0E04E4a402A2Ea20c0f637AEbF71F",
        "0x7D328F4E46f07033C6083E0D49194dAA9c2d733D",
        "0x50a72cB598cA622D5F82d8c4a257dad388e0764A"
    ]
# Address of the liquidRouter
LIQUID_ROUTER = "0x7F047E9D15b2a5937399f5F39e943A989D952aeD"

transactions = []
def file_transaction() :
    for i in addresses :
        transactions.append({
            "to":i,
            "value":"0",
            "data":None,
            "contractMethod":{
                "inputs":[
                    {
                        "name":"_claimer",
                        "type":"address"
                    }],
                "name":"set_claimer",
                "payable": False
            },
            "contractInputsValues":{"_claimer":LIQUID_ROUTER}
        })

file_transaction()

dictionary = {
    "version":"1.0",
    "version":"1.0",
    "chainId":"1",
    "createdAt":int(datetime.timestamp(datetime.now())),
    "meta":{
        "name":"Transactions Batch",
        "description":"",
        "txBuilderVersion":"1.11.1",
        "createdFromSafeAddress":"0xF930EBBd05eF8b25B1797b9b2109DDC9B0d43063",
        "createdFromOwnerAddress":"",
        "checksum":"0x694cb59ffe38bbe6cb79da20b48244771503b1fe6f2fad59de75115fb44c0ba4"
        },
    "transactions":transactions
}

json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("Transaction Batch.json", "w") as outfile:
    outfile.write(json_object)