primes = [5, 7, 11, 13, 19, 23, 29, 41, 43, 47,
            53, 61, 67, 73, 79, 83, 89, 97, 103, 109,
            113, 127, 131, 139, 151, 157, 163, 167, 173, 181,
            193, 199, 211, 223, 229, 233, 241, 251, 257, 263,
            271, 277, 283, 293, 307, 313, 317, 331, 337, 349,
            353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
            421, 433, 439, 443, 449, 457, 463, 467, 479, 487,
            491, 499, 503, 509, 523, 541, 547, 557, 563, 571,
            577, 587, 593, 601, 607, 613, 619, 631, 643, 647,
            653, 661, 673, 677, 683, 691, 701, 709, 719, 727,
            733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
            811, 823, 829, 839, 853, 859, 863, 877, 883, 887,
            907, 911, 919, 929, 937, 941, 947, 953, 967, 971,
            977, 983, 991, 997, 1009, 1013, 1021, 1033, 1039, 1051,
            1063, 1069, 1087, 1093, 1097, 1103, 1109, 1117, 1123, 1129,
            1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223,
            1231, 1237, 1249, 1259, 1279, 1283, 1291, 1297, 1303, 1307,
            1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1429,
            1433, 1439, 1447, 1453, 1459, 1471, 1483, 1489, 1493, 1499,
            1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579,
            1583, 1597, 1601, 1609, 1613, 1621, 1627, 1637, 1657, 1663,
            1669, 1693, 1699, 1709, 1723, 1733, 1741, 1747, 1753, 1759,
            1777, 1783, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867,
            1873, 1879, 1889, 1901, 1907, 1913, 1933, 1951, 1973, 1979,
            1987, 1993, 1999, 2003, 2011, 2017, 2029, 2039, 2053, 2063,
            2069, 2083, 2089, 2099, 2113, 2131, 2137, 2143, 2153, 2161,
            2179, 2203, 2207, 2213, 2221, 2239, 2243, 2251, 2269, 2273,
            2281, 2287, 2293, 2297, 2311, 2333, 2341, 2347, 2351, 2357,
            2371, 2377, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437,
            2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539,
            2543, 2551, 2557, 2579, 2593, 2609, 2617, 2621, 2633, 2647,
            2659, 2663, 2671, 2677, 2683, 2689, 2693, 2699, 2707, 2713,
            2719, 2731, 2741, 2749, 2753, 2767, 2777, 2791, 2797, 2803,
            2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897,
            2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2971, 3001,
            3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083,
            3089, 3109, 3121, 3137, 3163, 3169, 3181, 3187, 3191, 3203,
            3209, 3217, 3221, 3229, 3253, 3259, 3271, 3301, 3307, 3313,
            3319, 3323, 3331, 3343, 3347, 3361, 3373, 3391, 3407, 3413,
            3433, 3449, 3457, 3463, 3469, 3491, 3499, 3511, 3517, 3529,
            3533, 3541, 3547, 3559, 3571, 3583, 3593, 3607, 3613, 3617,
            3623, 3631, 3637, 3643, 3659, 3673, 3677, 3691, 3697, 3701,
            3709, 3719, 3727, 3733, 3739, 3761, 3769, 3779, 3793, 3797,
            3803, 3823, 3833, 3847, 3853, 3863, 3877, 3881, 3889, 3907,
            3911, 3919, 3923, 3931, 3943, 3947, 3967, 3989, 4003, 4007,
            4013, 4021, 4027, 4051, 4057, 4073, 4079, 4093, 4099, 4111,
            4129, 4133, 4139, 4153, 4159, 4177, 4201, 4211, 4219, 4231,
            4243, 4253, 4261, 4273, 4283, 4289, 4297, 4327, 4339, 4349,
            4357, 4363, 4373, 4391, 4397, 4409, 4423, 4441, 4447, 4451,
            4457, 4463, 4483, 4493, 4507, 4513, 4519, 4523, 4549, 4561,
            4567, 4583, 4591, 4597, 4603, 4621, 4639, 4643, 4651, 4657,
            4663, 4673, 4679, 4691, 4703, 4723, 4729, 4733, 4751, 4759,
            4783, 4789, 4793, 4801, 4813, 4817, 4831, 4861, 4871, 4877,
            4889, 4903, 4909, 4919, 4933, 4937, 4943, 4951, 4957, 4969,
            4973, 4987, 4993, 4999, 5003, 5011, 5023, 5039, 5051, 5059,
            5077, 5081, 5087, 5101, 5107, 5113, 5119, 5147, 5153, 5167,
            5171, 5179, 5189, 5197, 5209, 5227, 5233, 5237, 5261, 5273,
            5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387,
            5393, 5399, 5407, 5413, 5419, 5431, 5437, 5443, 5449, 5471,
            5479, 5483, 5503, 5507, 5521, 5527, 5531, 5557, 5563, 5569,
            5573, 5581, 5591, 5623, 5641, 5647, 5653, 5659, 5669, 5683,
            5689, 5693, 5701, 5711, 5717, 5737, 5743, 5749, 5779, 5801,
            5827, 5851, 5869, 5881, 5903, 5927, 5953, 5981, 6007, 6037,
            6067, 6091, 6113, 6133, 6143, 6173, 6199, 6217, 6247, 6271,
            6301, 6311, 6337, 6361, 6389, 6421, 6451, 6469, 6491, 6521,
            6553, 6577, 6607, 6637, 6661, 6691, 6703, 6733, 6763, 6781,
            6803, 6829, 6841, 6871, 6883, 6917, 6949, 6983, 7013, 7039,
            7069, 7103, 7129, 7151, 7177, 7213, 7247, 7283, 7309, 7333,
            7369, 7393, 7411, 7433, 7459, 7489, 7517, 7549, 7561, 7591,
            7621, 7649, 7687, 7723, 7759, 7789, 7817, 7841, 7879, 7883,
            7919, 7951, 7963, 7993, 8011, 8017, 8053, 8089, 8123, 8161,
            8191, 8221, 8233, 8263, 8293, 8317, 8353, 8389, 8431, 8461,
            8501, 8539, 8563, 8599, 8629, 8663, 8699, 8737, 8779, 8821,
            8863, 8887, 8929, 8971, 9013, 9049, 9091, 9127, 9157, 9199,
            9241, 9283, 9311, 9343, 9377, 9421, 9467, 9511, 9547, 9587,
            9631, 9679, 9721, 9769, 9811, 9859, 9883, 9931, 9967, 10009,
            10039, 10069, 10093, 10141, 10177, 10223, 10273, 10303, 10343, 10391,
            10429, 10459, 10501, 10531, 10567, 10613, 10663, 10711, 10729, 10781,
            10831, 10861, 10891, 10939, 10973, 11027, 11059, 11071, 11119, 11161,
            11197, 11243, 11299, 11353, 11383, 11437, 11491, 11497, 11551, 11579,
            11617, 11657, 11701, 11731, 11779, 11833, 11887, 11941, 11987, 12043,
            12073, 12109, 12163, 12197, 12241, 12263, 12323, 12379, 12421, 12479,
            12541, 12553, 12613, 12641, 12703, 12763, 12823, 12829, 12889, 12919,
            12941, 13003, 13037, 13099, 13159, 13219, 13229, 13291, 13339, 13399,
            13421, 13487, 13553, 13613, 13681, 13711, 13763, 13831, 13879, 13933,
            13999, 14029, 14083, 14143, 14197, 14251, 14281, 14323, 14389, 14449,
            14479, 14551, 14563, 14629, 14669, 14731, 14797, 14869, 14939, 15013,
            15073, 15139, 15199, 15271, 15331, 15373, 15439, 15511, 15583, 15661,
            15733, 15739, 15817, 15889, 15901, 15973, 15991, 16063, 16141, 16189,
            16231, 16301, 16363, 16381, 16453, 16477, 16553, 16633, 16693, 16747,
            16831, 16903, 16981, 17029, 17107, 17191, 17209, 17293, 17317, 17389,
            17419, 17497, 17581, 17599, 17683, 17749, 17791, 17839, 17911, 17959,
            18043, 18121, 18169, 18253, 18341, 18433, 18523, 18583, 18661, 18749,
            18839, 18913, 19001, 19081, 19141, 19213, 19289, 19381, 19471, 19543,
            19603, 19699, 19753, 19843, 19891, 19963, 20051, 20149, 20233, 20261,
            20359, 20443, 20479, 20551, 20641, 20719, 20809, 20899, 20983, 21013,
            21089, 21193, 21221, 21319, 21391, 21493, 21559, 21649, 21739, 21841,
            21929, 22039, 22093, 22171, 22273, 22381, 22483, 22543, 22639, 22751,
            22861, 22963, 23029, 23087, 23203, 23293, 23371, 23431, 23539, 23629,
            23743, 23833, 23911, 23993, 24109, 24181, 24281, 24373, 24469, 24571,
            24677, 24799, 24919, 24979, 25057, 25171, 25183, 25303, 25411, 25471,
            25579, 25673, 25801, 25849, 25933, 25999, 26113, 26141, 26251, 26309,
            26431, 26557, 26683, 26731, 26863, 26953, 27061, 27109, 27241, 27283,
            27409, 27481, 27583, 27691, 27793, 27919, 27961, 28099, 28183, 28279,
            28411, 28549, 28621, 28753, 28879, 29023, 29131, 29243, 29389, 29423,
            29569, 29671, 29761, 29881, 30013, 30139, 30271, 30391, 30469, 30559,
            30689, 30841, 30931, 31081, 31123, 31249, 31393, 31513, 31567, 31723,
            31873, 32029, 32143, 32299, 32413, 32563, 32719, 32833, 32911, 33073,
            33151, 33289, 33427, 33589, 33751, 33863, 34033, 34159, 34303, 34471,
            34591, 34759, 34843, 34963, 35107, 35281, 35449, 35593, 35731, 35839,
            36013, 36187, 36343, 36469, 36599, 36781, 36901, 37021, 37201, 37363,
            37549, 37693, 37813, 37993, 38053, 38239, 38329, 38449, 38569, 38749,
            38923, 39043, 39163, 39343, 39511, 39631, 39829, 39841, 40039, 40231,
            40429, 40531, 40699, 40849, 40939, 41143, 41233, 41413, 41611, 41761,
            41959, 42073, 42283, 42463, 42643, 42841, 43051, 43117, 43321, 43399,
            43579, 43783, 43891, 44029, 44203, 44383, 44533, 44701, 44909, 45121,
            45181, 45377, 45589, 45599, 45823, 46051, 46273, 46441, 46591, 46681,
            46831, 47059, 47149, 47353, 47431, 47659, 47881, 48121, 48313, 48541,
            48781, 48991, 49123, 49333, 49549, 49789, 50023, 50263, 50461, 50647,
            50893, 51061, 51241, 51481, 51721, 51829, 52069, 52291, 52543, 52711,
            52861, 53089, 53299, 53551, 53719, 53899, 54133, 54403, 54647, 54919,
            55051, 55219, 55441, 55663, 55933, 56209, 56479, 56713, 56911, 57193,
            57271, 57529, 57793, 57901, 58111, 58369, 58603, 58789, 59011, 59209,
            59359, 59629, 59791, 60091, 60353, 60649, 60889, 61153, 61381, 61673,
            61981, 62131, 62311, 62617, 62929, 63031, 63313, 63589, 63841, 64153,
            64303, 64579, 64879, 65173, 65449, 65701, 65839, 66109, 66361, 66571,
            66853, 67141, 67429, 67759, 67933, 68209, 68491, 68821, 69151, 69493,
            69829, 70123, 70381, 70573, 70921, 71263, 71473, 71809, 72169, 72469,
            72649, 72871, 73039, 73363, 73609, 73849, 74101, 74383, 74719, 75013,
            75169, 75391, 75619, 75991, 76261, 76543, 76873, 77239, 77419, 77761,
            78139, 78511, 78889, 79231, 79561, 79813, 80149, 80449, 80833, 81199,
            81553, 81901, 82141, 82531, 82891, 83233, 83641, 84061, 84391, 84811,
            85093, 85429, 85819, 86113, 86533, 86929, 87121, 87541, 87961, 88261,
            88663, 89083, 89521, 89599, 90019, 90373, 90679, 91081, 91369, 91813,
            92221, 92671, 93133, 93481, 93889, 94309, 94651, 95089, 95443, 95791,
            96181, 96589, 97003, 97369, 97843, 98299, 98641, 99133, 99529, 99991,
            100363, 100801, 101113, 101503, 102001, 102409, 102913, 103393, 103813, 104311,
            104761, 105229, 105529, 106033, 106543, 107071, 107509, 108013, 108463, 108949,
            109453, 109831, 110323, 110731, 111229, 111733, 112069, 112573, 113023, 113539,
            114043, 114601, 115021, 115471, 115981, 116533, 117043, 117619, 118171, 118621,
            119089, 119551, 120091, 120691, 120919, 121351, 121789, 122323, 122869, 123379,
            123733, 124303, 124909, 125509, 125899, 126493, 127081, 127711, 128341, 128971,
            129589, 130201, 130843, 131449, 132049, 132709, 133279, 133633, 134293, 134839,
            135391, 136069, 136693, 137341, 137869, 138181, 138799, 139303, 139969, 140419,
            140839, 141499, 142099, 142789, 143503, 144169, 144889, 145603, 146299, 146893,
            147451, 148153, 148861, 149563, 150301, 151051, 151771, 152533, 153271, 153889,
            154621, 155383, 156061, 156679, 157429, 158143, 158749, 159169, 159871, 160621,
            161341, 161971, 162751, 163411, 164149, 164839, 165553, 166303, 167023, 167779,
            168601, 169321, 170101, 170761, 171403, 172171, 173023, 173431, 174259, 175069,
            175939, 176791, 177679, 178489, 179383, 180181, 181003, 181759, 182659, 183571,
            184489, 185371, 186163, 187069, 187909, 188833, 189439, 190369, 191251, 192193,
            192889, 193813, 194683, 195343, 196171, 196993, 197959, 198943, 199933, 200869,
            201403, 202291, 203209, 204163, 205033, 205951, 206953, 207973, 208891, 209821,
            210811, 211663, 212671, 213289, 214213, 215143, 215983, 216901, 217909, 218719,
            219763, 220861, 221719, 222793, 223831, 224911, 225289, 226381, 227473, 228421,
            229549, 230563, 231613, 232711, 233689, 234811, 235789, 236869, 238039, 239233,
            240259, 241261, 242449, 243433, 244639, 245851, 247069, 248179, 249421, 250501,
            251611, 252829, 253951, 255193, 256471, 257689, 258919, 260191, 261433, 262741,
            263821, 265093, 266353, 267679, 268999, 270241, 271501, 272761, 274123, 275323,
            276589, 277789, 279121, 280339, 281719, 283099, 284509, 285841, 287239, 288649,
            290023, 291373, 292711, 294001, 295441, 296731, 298213, 299683, 301183, 302581,
            304069, 305479, 306949, 308491, 310021, 311569, 313129, 314599, 316033, 317593,
            319129, 320659, 322249, 323803, 325309, 326869, 328333, 329803, 331339, 332989,
            334333, 335809, 337489, 339139, 340789, 342469, 344173, 345601, 347299, 348991,
            350731, 352483, 354253, 355939, 357571, 359209, 360781, 362431, 364129, 365839,
            367651, 369409, 371143, 372943, 374641, 376471, 378151, 379681, 381529, 383419,
            385291, 387199, 389029, 390961, 392761, 394411, 396379, 398341, 400249, 402223,
            404191, 406171, 408211, 410119, 412033, 414019, 415951, 417961, 420001, 422089,
            423991, 426091, 428149, 430279, 432391, 434389, 436483, 438523, 440443, 442573,
            444793, 446893, 448999, 451183, 453199, 455263, 457279, 459469, 461689, 463891,
            466183, 468493, 470599, 472909, 475273, 477553, 479881, 482233, 484609, 486949,
            489241, 491503, 493813, 496231, 498403, 500809, 503233, 505513, 508021, 510553,
            513103, 515653, 518059, 520309, 522763, 525361, 525871, 528511, 531103, 533713,
            536059, 538711, 541363, 543889, 546619, 549163, 551911, 554641, 557371, 560083,
            562579, 565381, 568153, 570961, 573739, 576553, 579283, 582139, 585043, 587749,
            590659, 593323, 596293, 599149, 602083, 605023, 607933, 610921, 613969, 616789,
            619741, 622483, 625591, 628681, 631531, 634651, 637531, 640669, 643849, 646981,
            649879, 653113, 656323, 659611, 662773, 665983, 669289, 672643, 675979, 679363,
            682699, 686029, 689461, 692539, 695881, 699289, 702139, 705493, 708859, 712171,
            715441, 719011, 722539, 725863, 729271, 732829, 736471, 740143, 743779, 747451,
            751141, 754711, 758503, 762241, 765859, 769423, 773209, 777013, 780721, 784183,
            788089, 791803, 795763, 799741, 803731, 807733, 811651, 815413, 819391, 823483,
            827539, 831661, 835819, 839959, 844141, 848203, 852289, 856549, 860791, 865003,
            868999, 873319, 877621, 882019, 886429, 890863, 894793, 899161, 903451, 907969,
            912451, 916933, 921499, 926089, 930469, 934981, 939613, 944149, 948799, 953503,
            958051, 962671, 967321, 972163, 977023, 981601, 986509, 991429, 996409, 1001323,
            1006153, 1010983, 1016011, 1020709, 1025419, 1030441, 1035343, 1040449, 1045549, 1050739,
            1054441, 1059703, 1065013, 1070341, 1075621, 1080901, 1086103, 1091551, 1096969, 1102429,
            1107793, 1113319, 1118809, 1124269, 1129441, 1135009, 1140679, 1146331, 1151881, 1157491,
            1163233, 1168933, 1174783, 1180549, 1186351, 1192099, 1197829, 1203691, 1209631, 1215649,
            1221751, 1227703, 1233763, 1239739, 1245619, 1251871, 1257961, 1264261, 1270561, 1276621,
            1282513, 1288921, 1295389, 1301851, 1308301, 1314769, 1321303, 1327903, 1334119, 1340749,
            1347289, 1354009, 1360531, 1367341, 1374211, 1380889, 1387783, 1394671, 1401319, 1408009,
            1415083, 1421911, 1428673, 1435741, 1442923, 1449979, 1457149, 1464259, 1471501, 1478839,
            1486141, 1493449, 1500931, 1508473, 1515973, 1523443, 1530829, 1538503, 1546219, 1553809,
            1561423, 1569259, 1577101, 1584901, 1592863, 1600789, 1608823, 1616899, 1624969, 1633129,
            1641091, 1649311, 1657573, 1665649, 1673953, 1682251, 1690693, 1699069, 1707523, 1715851,
            1724449, 1732903, 1741321, 1749961, 1758739, 1767421, 1776241, 1785103, 1793719, 1802599,
            1811569, 1820551, 1829551, 1838521, 1847539, 1856821, 1865839, 1874923, 1884343, 1893589,
            1903063, 1912453, 1921921, 1931539, 1941091, 1950763, 1960531, 1970263, 1980031, 1989961,
            1999891, 2009869, 2019709, 2029723, 2039911, 2050033, 2060161, 2070463, 2080849, 2091151,
            2101249, 2111311, 2121739, 2131981, 2142643, 2153299, 2164039, 2174773, 2185699, 2196541,
            2207539, 2218429, 2229391, 2240479, 2251729, 2262643, 2273671, 2285071, 2296519, 2308003,
            2319409, 2330929, 2342611, 2354353, 2365999, 2377789, 2389591, 2401549, 2412409, 2424493,
            2436613, 2448829, 2461093, 2473423, 2485669, 2497933, 2510449, 2522659, 2534881, 2547583,
            2560213, 2573059, 2585953, 2598859, 2611909, 2624959, 2637961, 2651191, 2664451, 2677819,
            2690959, 2704393, 2717833, 2731429, 2745049, 2758843, 2772571, 2786221, 2800141, 2814169,
            2828299, 2842159, 2856379, 2870473, 2884573, 2898949, 2913193, 2927809, 2942521, 2957191,
            2972029, 2986561, 3001501, 3016549, 3031531, 3046081, 3061381, 3076393, 3091819, 3107329,
            3122881, 3138493, 3153949, 3169549, 3185263, 3201181, 3216979, 3232963, 3249151, 3265441,
            3281689, 3297859, 3314413, 3330961, 3347263, 3363793, 3380551, 3397003, 3413791, 3430633,
            3447349, 3464431, 3481801, 3499261, 3516553, 3533359, 3551029, 3568783, 3586549, 3604543,
            3622261, 3640333, 3658429, 3676639, 3694843, 3713263, 3731869, 3750613, 3769069, 3787969,
            3806839, 3825853, 3845029, 3863683, 3882913, 3902419, 3921193, 3940801, 3960499, 3980401,
            4000303, 4020283, 4040431, 4060633, 4080943, 4101289, 4121869, 4142311, 4162861, 4183693,
            4204441, 4225549, 4246681, 4267891, 4289101, 4310563, 4332091, 4353823, 4375669, 4396783,
            4418749, 4440901, 4463191, 4485589, 4508029, 4530499, 4553113, 4575973, 4598941, 4621951,
            4644853, 4667983, 4691383, 4714861, 4738423, 4762213, 4786051, 4809943, 4833991, 4858081,
            4881871, 4906333, 4930951, 4955479, 4980193, 5005129, 5030101, 5055361, 5080711, 5105923,
            5130949, 5156551, 5182453, 5208481, 5234269, 5260561, 5286553, 5313043, 5339671, 5366401,
            5393329, 5420119, 5446741, 5473879, 5501059, 5528389, 5556079, 5583889, 5611843, 5639929,
            5667973, 5696293, 5724613, 5753353, 5782201, 5811121, 5840041, 5869351, 5898691, 5928049,
            5957641, 5987551, 6017581, 6047731, 6078073, 6108439, 6139123, 6169909, 6200863, 6231751,
            6262759, 6294091, 6325303, 6356923, 6388861, 6420961, 6453199, 6485209, 6517759, 6550501,
            6583351, 6616399, 6649483, 6682861, 6715771, 6749263, 6783151, 6816853, 6850999, 6885409,
            6919723, 6954319, 6989113, 7024183, 7059253, 7094671, 7130119, 7165663, 7201633, 7237819,
            7273993, 7310353, 7346953, 7383283, 7420339, 7457479, 7494871, 7532251, 7570009, 7607881,
            7646029, 7684423, 7722943, 7761409, 7800139, 7839199, 7878319, 7917601, 7957351, 7997203,
            8037319, 8077171, 8117509, 8158063, 8198791, 8239423, 8280739, 8322241, 8363353, 8405209,
            8434609, 8476801, 8518933, 8561479, 8604469, 8647699, 8690953, 8734513, 8778391, 8822161,
            8866441, 8910973, 8955703, 9000379, 9045301, 9090691, 9135883, 9181789, 9227851, 9274051,
            9320323, 9366859, 9413881, 9461173, 9508693, 9556441, 9604039, 9652231, 9700543, 9748861,
            9797773, 9847003, 9896443, 9946171, 9995989, 10046173, 10096549, 10147003, 10197703, 10248829,
            10300273, 10351711, 10403671, 10455883, 10508293, 10560883, 10613929, 10666921, 10719829, 10773619,
            10827541, 10881679, 10936033, 10990783, 11046001, 11101471, 11157193, 11213143, 11269189, 11325241,
            11381863, 11438839, 11496049, 11553403, 11611429, 11669731, 11728273, 11786809, 11845819, 11905261,
            11965069, 12025129, 12085519, 12146053, 12206743, 12267889, 12329533, 12391429, 12453589, 12516013,
            12578803, 12641809, 12705313, 12768799, 12832903, 12897013, 12961471, 13026283, 13091191, 13156903,
            13222873, 13289233, 13355989, 13422769, 13490203, 13557751, 13625851, 13694203, 13762951, 13832011,
            13901431, 13971103, 14041009, 14111551, 14182171, 14253313, 14324419, 14395783, 14468119, 14540791,
            14613721, 14687011, 14760751, 14834623, 14908549, 14983093, 15058273, 15133873, 15209743, 15286093,
            15362863, 15440023, 15517591, 15595441, 15673771, 15752119, 15831253, 15910651, 15990553, 16070701,
            16151299, 16232131, 16313683, 16395061, 16477081, 16559791, 16642741, 16726363, 16810303, 16856011,
            16940221, 17025289, 17110351, 17196211, 17282569, 17369413, 17456191, 17543719, 17631769, 17720359,
            17809333, 17898823, 17987791, 18078031, 18168793, 18260071, 18351733, 18443839, 18536491, 18629491,
            18722983, 18816181, 18910501, 19005361, 19100449, 19196293, 19292731, 19389613, 19486969, 19584871,
            19683283, 19781989, 19881079, 19980811, 20081053, 20181949, 20283121, 20384911, 20487109, 20589631,
            20693083, 20796781, 20900443, 21005401, 21110863, 21216553, 21323089, 21429559, 21536761, 21644881,
            21753631, 21862573, 21971899, 22081981, 22192813, 22304131, 22416091, 22528399, 22641319, 22754749,
            22868983, 22983811, 23099203, 23215279, 23331589, 23448541, 23566159, 23684473, 23803363, 23922949,
            24043093, 24163693, 24284929, 24406729, 24528991, 24652129, 24775939, 24900391, 25025461, 25150903,
            25276549, 25403113, 25530709, 25658431, 25786729, 25916251, 26046103, 26176951, 26308201, 26440291,
            26573083, 26705893, 26839429, 26974039, 27109363, 27245461, 27382339, 27519829, 27658063, 27796843,
            27936511, 28076569, 28217509, 28358131, 28500631, 28643689, 28787569, 28932049, 29077381, 29223373,
            29369701, 29517283, 29665501, 29814559, 29964301, 30114433, 30265639, 30417721, 30570019, 30723421,
            30877669, 31032709, 31188571, 31345219, 31502563, 31660621, 31819561, 31979203, 32139553, 32300623,
            32462791, 32625781, 32789593, 32954083, 33118849, 33284893, 33452119, 33619981, 33691213, 33860443,
            34030333, 34201051, 34372909, 34545523, 34719079, 34893349, 35068531, 35244721, 35421769, 35598583,
            35777239, 35956519, 36137203, 36318553, 36501013, 36684409, 36868681, 37053691, 37239583, 37426693,
            37614571, 37803583, 37993093, 38183869, 38374939, 38567449, 38761213, 38955913, 39151549, 39348121,
            39545731, 39744043, 39943699, 40143991, 40345621, 40548229, 40751761, 40956361, 41162041, 41368543,
            41576413, 41785171, 41995003, 42206029, 42418093, 42630439, 42844579, 43059769, 43276111, 43493173,
            43711513, 43931161, 44151799, 44373391, 44596159, 44819713, 45044719, 45270811, 45498121, 45726259,
            45955453, 46186381, 46418329, 46651543, 46885843, 47120701, 47357269, 47595103, 47833783, 48073813,
            48315259, 48557851, 48801829, 49047043, 49293403, 49541029, 49789771, 50039851, 50290993, 50543179,
            50796679, 51051703, 51307519, 51565291, 51824263, 52084579, 52346029, 52608979, 52873129, 53138779,
            53405743, 53673931, 53943553, 54214339, 54486403, 54759409, 55034533, 55310779, 55588531, 55867291,
            56147701, 56429671, 56712841, 56997763, 57283909, 57571603, 57860839, 58151539, 58443733, 58737253,
            59031811, 59328163, 59626243, 59925871, 60226759, 60528733, 60832789, 61138243, 61445383, 61754041,
            62064253, 62374579, 62687743, 63002371, 63318331, 63636373, 63955561, 64276909, 64599583, 64923823,
            65249803, 65577331, 65906851, 66237949, 66570601, 66904969, 67240993, 67354951, 67692799, 68032933,
            68374729, 68718061, 69063079, 69410071, 69758791, 70108279, 70460521, 70814533, 71170249, 71527831,
            71887141, 72247999, 72611053, 72975439, 73341679, 73709863, 74080213, 74452363, 74826223, 75202009,
            75579733, 75959461, 76341121, 76724731, 77110213, 77497039, 77886409, 78277183, 78670309, 79065451,
            79462729, 79861759, 80262841, 80666143, 81071413, 81478753, 81888181, 82299643, 82713049, 83128429,
            83546011, 83965813, 84387661, 84811681, 85237771, 85665859, 86096029, 86528131, 86962903, 87399889,
            87839041, 88280191, 88723423, 89169193, 89616973, 90067093, 90519589, 90974173, 91430611, 91889929,
            92351629, 92815693, 93282019, 93750493, 94220941, 94694323, 95169673, 95647861, 96128323, 96611299,
            97096579, 97584493, 98074729, 98567473, 99062731, 99559951, 100060111, 100562851, 101067853, 101575711,
            102086059, 102598921, 103114483, 103632469, 104153221, 104676421, 105202423, 105730831, 106262131, 106796101,
            107332723, 107872069, 108414001, 108958543, 109505971, 110056099, 110609071, 111164863, 111723421, 112284589,
            112848763, 113415751, 113985301, 114557701, 115133311, 115711723, 116293171, 116877181, 117464353, 118053283,
            118646461, 119242549, 119841481, 120443461, 121048693, 121656739, 122268073, 122882449, 123499003, 124119511,
            124743139, 125369971, 125999569, 126632161, 127268461, 127907839, 128550553, 129196429, 129845503, 130497319,
            131152759, 131811709, 132473839, 133139473, 133808473, 134479903, 134694733, 135371179, 136051063, 136734373,
            137421331, 138111499, 138805363, 139501963, 140202529, 140906959, 141615013, 142325851, 143040439, 143758663,
            144481063, 145206961, 145935721, 146668243, 147405199, 148145863, 148890193, 149638261, 150390133, 151145263,
            151904761, 152668003, 153435133, 154205533, 154980403, 155758909, 156541603, 157328209, 158118601, 158912989,
            159711529, 160513963, 161320519, 162130849, 162945511, 163764313, 164587021, 165413959, 166244863, 167080189,
            167919379, 168762499, 169610041, 170462251, 171318733, 172179619, 173044519, 173913739, 174787621, 175665823,
            176548243, 177435301, 178326901, 179222809, 180123343, 181028119, 181937803, 182851939, 183770341, 184693573,
            185621299, 186553819, 187491151, 188432941, 189378769, 190330099, 191286343, 192247459, 193213201, 194183989,
            195159403, 196139599, 197125069, 198115573, 199111039, 200111533, 201116791, 202127209, 203142829, 204163639,
            205189561, 206220571, 207256813, 208298119, 209344351, 210396211, 211453381, 212515843, 213583759, 214656751,
            215735341, 216818281, 217907761, 219002671, 220102789, 221208331, 222319501, 223436401, 224559163, 225687589,
            226821229, 227960731, 229106071, 230257123, 231413629, 232576273, 233744521, 234918919, 236099251, 237285619,
            238477999, 239676289, 240880333, 242090551, 243307063, 244529671, 245758399, 246992959, 248233831, 249480769,
            250734373, 251994271, 253260439, 254533003, 255811951, 257097109, 258388681, 259687069, 260991631, 262303051,
            263621053, 264945679, 266277061, 267615013, 268959793, 269366371, 270719929, 272080201, 273447289, 274820479,
            276200791, 277588039, 278982751, 280384549, 281793469, 283208953, 284632099, 286062223, 287499493, 288943939,
            290395711, 291854671, 293320903, 294794701, 296276011, 297764479, 299260651, 300764293, 302275663, 303794431,
            305320579, 306854761, 308396653, 309946381, 311503783, 313069069, 314641333, 316222273, 317810749, 319407661,
            321011569, 322624651, 324245731, 325874779, 327511969, 329157739, 330811069, 332473123, 334143769, 335822833,
            337509631, 339205483, 340910023, 342622831, 344343733, 346073911, 347812393, 349559869, 351316351, 353081683,
            354855901, 356638651, 358430623, 360231691, 362041399, 363860269, 365688691, 367526209, 369373009, 371229151,
            373094593, 374969383, 376853293, 378746659, 380649883, 382562629, 384485029, 386416993, 388358629, 390309529,
            392270113, 394241251, 396221701, 398212681, 400213483, 402223741, 404244901, 406276231, 408317389, 410369233,
            412431199, 414503431, 416586301, 418679581, 420783073, 422897539, 425022583, 427158343, 429304783, 431461951,
            433629811, 435808693, 437998669, 440199589, 442411549, 444634693, 446868889, 449114089, 451370869, 453638599,
            455917621, 458208523, 460511071, 462824863, 465149809, 467486599, 469835623, 472196521, 474569341, 476953951,
            479350519, 481759171, 484179769, 486612523, 489057631, 491515099, 493984111, 496465969, 498960733, 501467809,
            503987611, 506520169, 509064793, 511622851, 514193761, 516777451, 519374239, 521983993, 524606941, 527242789,
            529891759, 532554499, 535230391, 537919903, 538712809, 541419889, 544140343, 546874453, 549622441, 552383593,
            555159223, 557948539, 560752141, 563569933, 566401489, 569247589, 572107609, 574982299, 577871479, 580775341,
            583693603, 586626619, 589574233, 592536229, 595513663, 598505881, 601513303, 604535809, 607572841, 610625581,
            613693963, 616777573, 619876603, 622991143, 626121721, 629267923, 632430061, 635607979, 638801521, 642011473,
            645237643, 648479833, 651738169, 655013143, 658304401, 661612099, 664935241, 668276449, 671634169, 675009079,
            678400519, 681809503, 685235281, 688678513, 692138929, 695616841, 699111949, 702624523, 706155091, 709703461,
            713269771, 716853589, 720455371, 724075663, 727713673, 731370319, 735045211, 738738901, 742450801, 746181589,
            749931211, 753699631, 757486843, 761293279, 765118729, 768963511, 772826779, 776710003, 780613051, 784535503,
            788477863, 792439933, 796422019, 800423653, 804444703, 808486873, 812548801, 816631429, 820734979, 824858941,
            829003729, 833168719, 837354853, 841562173, 845790973, 850040623, 854311849, 858604729, 862919209, 867255373,
            871613419, 875993023, 880394833, 884818843, 889264723, 893733361, 898223773, 902737273, 907273363, 911831359,
            916413361, 921018271, 925645813, 930296431, 934970209, 939667273, 944388943, 949134451, 953903791, 958697191,
            963514621, 968356201, 973222111, 978112363, 983027209, 987966901, 992931169, 997920613, 1002934549, 1007974153,
            1013037943, 1018127989, 1023244153, 1028385781, 1033553221, 1038746899, 1043966461, 1049211859, 1054484149, 1059782413,
            1065107839, 1070460121, 1075839133, 1080698989, 1086129493, 1091587129, 1097071993, 1102584451, 1108124869, 1113693313,
            1119289609, 1124914129, 1130566753, 1136247769, 1141957519, 1147695613, 1153462423, 1159258129, 1165082839, 1170937309,
            1176820819, 1182733753, 1188677131, 1194650203, 1200653173, 1206686359, 1212749611, 1218843289, 1224968011, 1231123549,
            1237309939, 1243527541, 1249775539, 1256055793, 1262366803, 1268710321, 1275085741, 1281493069, 1287932533, 1294402693,
            1300907011, 1307443201, 1314013033, 1320615799, 1327251883, 1333921489, 1340623969, 1347360061, 1354130431, 1360934293,
            1367772799, 1374645871, 1381553191, 1388495491, 1395472789, 1402485181, 1409532601, 1416615271, 1423733371, 1430887489,
            1438077703, 1445304169, 1452565993, 1459864999, 1467200599, 1474573279, 1481982811, 1489429093, 1496913193, 1504435171,
            1511994313, 1519592119, 1527227953, 1534902373, 1542615253, 1550365879, 1558156531, 1565986393, 1573855603, 1581763543,
            1589711413, 1597699843, 1605728473, 1613797399, 1621906501, 1630056361, 1638247339, 1646479663, 1654753171, 1663067983,
            1671424453, 1679823529, 1688264821, 1696747933, 1705274281, 1713842971, 1722455041, 1731110413, 1739809453, 1748552191,
            1757338801, 1766169469, 1775044321, 1783964011, 1792928563, 1801937551, 1810991953, 1820092411, 1829238529, 1838430049,
            1847668261, 1856952901, 1866284053, 1875661441, 1885086211, 1894558849, 1904078509, 1913646613, 1923262879, 1932927301,
            1942639969, 1952401513, 1962212209, 1972072309, 1981982089, 1991941621, 2001951313, 2012011093, 2022121249, 2032282633,
            2042495071, 2052758821, 2063074129, 2073441199, 2083860043, 2094331663, 2104854991, 2115431809, 2126062051, 2136745621
    ]


def desired_primes():
    huehue = [[0]]
    print(primes)
    for i in range(len(primes)):
        if i % 50 == 0:
            if ((primes[i] - 3) % 4) == 0:
                huehue.append(primes[i])
                print(primes[i])
    return huehue

if __name__ == "__main__":
    print(desired_primes())
