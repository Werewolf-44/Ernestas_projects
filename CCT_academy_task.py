"""
The calculations below are from a reference point at 0m. So there is an exponential decrease in lumination intensity the further the street light is from the begining of the road. 
Reference point was not clearly stated in the description but I assumed based on the notes. All in all, with the information provided, the street light with the lowest lumination 
will be at index 10, given that there are no 3 non-working street lights in a row before.

Made comments for myself, but decided to leave them in order to show my way of thinking, what and why I did it. Moreover, thank you for the task. It was fun in trying to tackle it.
Hope the logic is sound! 
"""

# Given formula for calculating lumination intensity.
def lumination_intensity(distance):
    return 3 ** (-(distance / 100) ** 2)

def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:

# If a road length is less than 20 there is only one street light
    if road_length < 20:
        if light in not_working_street_lights:
            return "Provided road length is less than 20m. There is only one street light at index 0 and it is not working. Please replace the bulb."
        else:
             return "Provided road length is less than 20m. There is only one street light at index 0 and it is working."
 # If the road length provided is over 2000000       
    if road_length > 2000000:
         raise ValueError("Provided road length exceeds maximum length. Please provide road with a length of 2000000 or less.")
    
    darkest_street_light_index = None 
    number_street_lights = road_length // 20 #// is to devide road_length by 20 and round it up to a nearest whole number get the number of street lights in a given road_length.
    lowest_lumination = float('inf') # Any positive number to infinity.

    # Iterate through all street lights

    for light in range(number_street_lights + 1): # We need to add +1 because one street light is at index 0.
            distance = light * 20 # We calculate the distance from the start for every street light.
            if light in not_working_street_lights and (light - 1) in not_working_street_lights and (light + 1) in not_working_street_lights:
                return light # if a given light is not working and is between 2 also non-working street lights - it will have the lowest lumination.

            lumination = lumination_intensity(distance) # Calculate the lumination based on distance.
            
            if lumination < 0.01:  # We ignore street lights that has lumination lower than 0.01.
                continue
            
            # We update darkest_street_light_index with lowest lumination that we find.
            if lumination < lowest_lumination:
                lowest_lumination = lumination
                darkest_street_light_index = light
                       
    return f"The street light with the lowest illumination intensity is at index {darkest_street_light_index}. Please replace the light bulb."


# Testing with different road lenghts and not working street lights

#print(find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[0, 2, 4, 5, 7, 9, 10]))
#print(find_index_of_darkest_street_light(road_length=400, not_working_street_lights=[2, 6, 15]))
#print(find_index_of_darkest_street_light(road_length=2000001, not_working_street_lights=[2, 5, 7, 9]))


"""
Optional (for extra Karma points): 
Please find the minimal number of light bulbs, which is needed to be replaced to make illumination intencity at every street light non less than 1.

My answer and way of thinking: 

I do not think this is achievable with given information and formula. The luminosity intensity is based on a distance and has an opposite relationship: if distance increases 
the luminosity intensity decreases. It was stated that all street lamps have the same luminosity intensity, which means, that first street light at an index of 0 and at 0 m of 
distance will have luminosity intensity of 1. We can assume that all of the street lamps have the same luminosity (except for those, that are not working and are provided in a 
not_working_street_lights list). With that said, for a person that stands at a street light with an index 0, at 0 m, only one street light will have luminosity of 1. Every other 
street light will have lower and cannot reach 1 with given conditions.

If you are at a static position luminosity for other street lights can only become 1 if you use different tools, like stronger light bulbs. The further the street light is from you
the stronger light bulb you would need in order to keep luminosity at 1 from your point of view. Or, you would have to be at every street light all at once...

If we throw out a person logic completely and just focus on the street lights - in order to achieve a luminosity of 1 for every street light, just replace all bulbs for 
those street lights that are not working and are provided in not_working_street_lights list. That way every street light will have luminosity of 1.
"""

"""
if __name__ == "__main__":
    # This is an example test. When evaluating the task, more will be added:
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6])
    print("ALL TESTS PASSED")
"""