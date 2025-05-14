


# import requests as r

# def soil_report(latitude, longitude):

#     R = r.get(f"https://soil.narc.gov.np/soil/api/?lat={latitude}&lon={longitude}").json()

#     if R:
#       try:
#         response= f'''
#         print(f"🧾 Soil Report for {R['palika']}, {R['district']} District, {R['province']} Province\n")

#         print("📍 Location Details:")
#         print(f"  Latitude  : {R['coord']['lat']}")
#         print(f"  Longitude : {R['coord']['lon']}")
#         print(f"  Elevation : {R['coord']['elevation']} m")

#         print("🌱 Soil Composition:")
#         print(f"  pH                 : {R['ph']}")
#         print(f"  Organic Matter     : {R['organic_matter']}")
#         print(f"  Total Nitrogen     : {R['total_nitrogen']}")
#         print(f"  Potassium (K)      : {R['potassium']}")
#         print(f"  Phosphorus (P₂O₅)  : {R['p2o5']}")
#         print(f"  Boron              : {R['boron'][0:4] +' mg/kg'}")
#         print(f"  Zinc               : {R['zinc'][0:4] +' mg/kg'}")

#         print("🧱 Soil Texture:")
#         print(f"  Sand  : {R['sand']}")
#         print(f"  Clay  : {R['clay']}")
#         print(f"  Silt  : {R['slit']}\n")

#         print("🪨 Parent Material:")
#         print(f"  {R['parentsoil']}")

#         '''

#         return response 


#       except:

#         return "The soil information is not available."








import requests as r

def soil_data_fetch(latitude, longitude):
    try:
        R = r.get(f"https://soil.narc.gov.np/soil/api/?lat={latitude}&lon={longitude}").json()

        if not R or 'coord' not in R:
            print("Soil data not available.")
            return "❌ The soil information is not available."

        print("Soil data fetched successfully.")  

        
        response = (
            f"🧾 Soil Report for {R['palika']}, {R['district']} District, {R['province']} Province\n\n"

            "📍 Location Details:\n"
            f"  Latitude  : {R['coord']['lat']}\n"
            f"  Longitude : {R['coord']['lon']}\n"
            f"  Elevation : {R['coord']['elevation']} m\n\n"

            "🌱 Soil Composition:\n"
            f"  pH                 : {R['ph']}\n"
            f"  Organic Matter     : {R['organic_matter']}\n"
            f"  Total Nitrogen     : {R['total_nitrogen']}\n"
            f"  Potassium (K)      : {R['potassium']}\n"
            f"  Phosphorus (P₂O₅)  : {R['p2o5']}\n"
            f"  Boron              : {R['boron'][0:4] +' mg/kg'}\n"
            f"  Zinc               : {R['zinc'][0:4] +' mg/kg'}\n"


            "🧱 Soil Texture:\n"
            f"  Sand  : {R['sand']}\n"
            f"  Clay  : {R['clay']}\n"
            f"  Silt  : {R['slit']}\n\n"

            "🪨 Parent Material:\n"
            f"  {R['parentsoil']}\n"
        )

        # print(response)


        return response

    except Exception as e:
        return f"❌ Failed to fetch soil report: {e}"

