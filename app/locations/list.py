from orbit_predictor.locations import *

##TODO FIX performance ... and required a new data structure
LOCATION_ENABLED=('AFRICA1' ,
                    'AFRICA2' ,
                    'AFRICA3' ,
                    'AFRICA4' ,
                    'AFRICA5' ,
                    'AMERICA1' ,
                    'AMERICA10' ,
                    'AMERICA11' ,
                    'AMERICA2' ,
                    'AMERICA3' ,
                    'AMERICA4' ,
                    'AMERICA5' ,
                    'AMERICA6' ,
                    'AMERICA7' ,
                    'AMERICA8' ,
                    'AMERICA9' ,
                    'ARG' ,
                    'ASIA1' ,
                    'ASIA10' ,
                    'ASIA11' ,
                    'ASIA12' ,
                    'ASIA13' ,
                    'ASIA14' ,
                    'ASIA15' ,
                    'ASIA16' ,
                    'ASIA17' ,
                    'ASIA18' ,
                    'ASIA19' ,
                    'ASIA2' ,
                    'ASIA3' ,
                    'ASIA4',
                    'ASIA5' ,
                    'ASIA6' ,
                    'ASIA7' ,
                    'ASIA8' ,
                    'ASIA9' ,
                    'AUSTRALIA1' ,
                    'AUSTRALIA2' ,
                    'AUSTRALIA5' ,
                    'AUSTRALIA6' ,
                    'AUSTRALIA7' ,
                    'BA1' ,
                    'CHILE',
                    'EASTER_ISLAND' ,
                    'EUROPA1' ,
                    'EUROPA10' ,
                    'EUROPA11' ,
                    'EUROPA12' ,
                    'EUROPA13' ,
                    'EUROPA14' ,
                    'EUROPA15' ,
                    'EUROPA16' ,
                    'EUROPA17' ,
                    'EUROPA3' ,
                    'EUROPA5' ,
                    'EUROPA7' ,
                    'EUROPA9' ,
                    'MADAGASCAR1' ,
                    'MADAGASCAR2' ,
                    'NZ1' ,
                    'NZ2' ,
                    'RIO' ,
                    'USA' ,
                    'australia' ,
                    'brazil' ,
                    'blq_leafline' ,
                    'central_america' ,
                    'central_argentina' ,
                    'china' ,
                    'eastern_russia' ,
                    'france',
                    'germany' ,
                    'india' ,
                    'moscu' ,
                    'niger' ,
                    'riogrande')

LOCATIONS_GET={'AFRICA1':AFRICA1,
                    'AFRICA2':AFRICA2,
                    'AFRICA3':AFRICA3,
                    'AFRICA4':AFRICA4,
                    'AFRICA5':AFRICA5,
                    'AMERICA1':AMERICA1,
                    'AMERICA10':AMERICA10 ,
                    'AMERICA11':AMERICA11 ,
                    'AMERICA2':AMERICA2,
                    'AMERICA3':AMERICA3 ,
                    'AMERICA4':AMERICA4 ,
                    'AMERICA5':AMERICA5 ,
                    'AMERICA6':AMERICA6 ,
                    'AMERICA7':AMERICA7 ,
                    'AMERICA8':AMERICA8 ,
                    'AMERICA9':AMERICA9 ,
                    'ARG':ARG,
                    'ASIA1':ASIA1 ,
                    'ASIA10':ASIA10 ,
                    'ASIA11':ASIA11 ,
                    'ASIA12':ASIA12 ,
                    'ASIA13':ASIA13 ,
                    'ASIA14':ASIA14 ,
                    'ASIA15':ASIA15 ,
                    'ASIA16':ASIA16 ,
                    'ASIA17':ASIA17 ,
                    'ASIA18':ASIA18 ,
                    'ASIA19':ASIA19 ,
                    'ASIA2':ASIA2 ,
                    'ASIA3':ASIA3 ,
                    'ASIA4':ASIA4,
                    'ASIA5':ASIA5 ,
                    'ASIA6':ASIA6 ,
                    'ASIA7':ASIA7 ,
                    'ASIA8':ASIA8 ,
                    'ASIA9':ASIA9 ,
                    'AUSTRALIA1':AUSTRALIA1 ,
                    'AUSTRALIA2':AUSTRALIA2 ,
                    'AUSTRALIA5':AUSTRALIA5 ,
                    'AUSTRALIA6':AUSTRALIA6 ,
                    'AUSTRALIA7':AUSTRALIA7 ,
                    'BA1':BA1,
                    'CHILE':CHILE,
                    'EASTER_ISLAND':EASTER_ISLAND ,
                    'EUROPA1':EUROPA1,
                    'EUROPA10':EUROPA10,
                    'EUROPA11':EUROPA11 ,
                    'EUROPA12':EUROPA12 ,
                    'EUROPA13':EUROPA13 ,
                    'EUROPA14':EUROPA14 ,
                    'EUROPA15':EUROPA15 ,
                    'EUROPA16':EUROPA16 ,
                    'EUROPA17':EUROPA17 ,
                    'EUROPA3':EUROPA3 ,
                    'EUROPA5':EUROPA5 ,
                    'EUROPA7':EUROPA7 ,
                    'EUROPA9':EUROPA9 ,
                    'MADAGASCAR1':MADAGASCAR1 ,
                    'MADAGASCAR2':MADAGASCAR2 ,
                    'NZ1':NZ1 ,
                    'NZ2':NZ2 ,
                    'RIO':RIO ,
                    'USA':USA ,
                    'australia':australia ,
                    'brazil':brazil ,
                    'blq_leafline':blq_leafline ,
                    'central_america':central_america ,
                    'central_argentina':central_argentina ,
                    'china':china ,
                    'eastern_russia':eastern_russia ,
                    'france':france,
                    'germany':germany,
                    'india':india ,
                    'moscu':moscu ,
                    'niger':niger ,
                    'riogrande':riogrande
                    }