import csv

rows = [
['SICKO MODE','Travis Scott','2xLMifQCjDGFmkHkpNLD9h',155,8,1,0.85,0.43],
['DNA.','Kendrick Lamar','6HZILIRieu8S0iqY8kIKhj',140,1,1,0.80,0.38],
['goosebumps','Travis Scott','6gBFPUFcJLzWGx4lenP6h2',130,7,1,0.78,0.42],
['bad guy','Billie Eilish','2Fxmhks0bxGSBdJ92vM42m',135,7,1,0.65,0.56],
['Lose Yourself','Eminem','5Z01UMMf7V1o0MzF86s6WJ',171,0,0,0.92,0.28],
['Till I Collapse','Eminem','4xkOaSrkexMciUUogZKVTS',171,1,1,0.94,0.22],
['Power','Kanye West','2gZUPNdnz5Y45eiGxpHGSc',130,8,0,0.55,0.28],
['Die For You','The Weeknd','2Ch7LmS7r2Gy2kc64wv3Bz',134,1,0,0.52,0.33],
['Adore You','Harry Styles','3jjujdWJ72nww5eGnfs2E7',99,8,1,0.67,0.72],
['Watermelon Sugar','Harry Styles','6UelLqGlWMcVH1E5c4H7lY',95,7,1,0.82,0.80],
["Can't Feel My Face",'The Weeknd','22VdIZQfgXJea34mQxlt81',93,11,1,0.74,0.61],
["God's Plan",'Drake','5ZKG94fnjiuMH5yrC5S9lS',77,8,1,0.64,0.44],
['Mask Off','Future','2Ch7LmS7r2Gy2kc64wv3Bz',150,9,0,0.75,0.34],
['Stay','The Kid LAROI','5kKkqTY9HfNYtAUZXPuImt',170,11,1,0.76,0.83],
]

with open('songs.csv','a',newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
print('Done! Added', len(rows), 'songs')
