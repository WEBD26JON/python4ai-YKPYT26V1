```python
COLUMN_INFO = {
    "Age": "age",               
    # Patientens ålder i år

    "Sex": "sex",               
    # Kön: 1 = man, 0 = kvinna

    "ChestPain": "chest_pain",  
    # Typ av bröstsmärta:
    # typisk (klassisk hjärtsmärta),
    # atypisk,
    # icke-hjärtrelaterad (non-anginal),
    # asymtomatisk (ingen smärta trots sjukdom)

    "RestBP": "rbl_pres",       
    # Viloblodtryck (mm Hg), dvs blodtrycket när patienten är i vila

    "Chol": "chol",             
    # Kolesterolnivå i blodet

    "Fbs": "fbl_sugar",         
    # Fastande blodsocker > 120 mg/dl
    # 1 = högt värde, 0 = normalt

    "RestECG": "rest_ecg",      
    # Resultat från EKG i vila (hjärtats elektriska aktivitet)

    "MaxHR": "max_hr",          
    # Maximal hjärtfrekvens uppnådd under belastningstest

    "ExAng": "ex_angina",       
    # Ansträngningsutlöst kärlkramp
    # (bröstsmärta som uppstår vid fysisk aktivitet)

    "Oldpeak": "oldpeak",       
    # ST-sänkning under belastning
    # Visar hur mycket hjärtats signal förändras vid stress
    # Höga värden tyder på syrebrist i hjärtat

    "Slope": "st_slope",        
    # Lutningen på ST-segmentet under belastning
    # Beskriver formen på EKG-kurvan vid maximal ansträngning

    "Ca": "ca",                 
    # Antal större blodkärl (0–3) som visar förträngning
    # Högre värde = fler påverkade kärl

    "Thal": "thal",             
    # Resultat från ett test av blodflödet i hjärtat:
    # normal = normalt blodflöde
    # fixed defect = permanent skada
    # reversible defect = problem vid belastning

    "AHD": "ahd"                
    # Förekomst av hjärtsjukdom (målvariabel)
    # Yes/No → senare omvandlat till 1/0
}
```
