import requests
import statistics

def get_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Request failed")
        return None

def calculate_population_density(country):
    if 'population' in country and 'area' in country:
        population = country['population']
        area = country['area']
        if area == 0:
            return 0
        else:
            return population / area
    else:
        return None

def main():
    country_data = get_data()
    if country_data:
        population_densities = []
        un_members = 0
        euro_users = 0
        
        for country in country_data:
            if 'name' in country:
                country_name = country['name']['common']
                population_density = calculate_population_density(country)
                if population_density is not None:
                    population_densities.append(population_density)
                    
                if 'unMember' in country and country['unMember']:
                    un_members += 1
                    
                if 'currencies' in country and 'EUR' in country['currencies']:
                    euro_users += 1
                    
                print(f"{country_name} has {population_density:.2f} people per sq km")
        
# Calculating mean, median, and standard deviation
        mean_den = statistics.mean(population_densities)
        median_den = statistics.median(population_densities)
        std_dev_den = statistics.stdev(population_densities)
        
        print("\nMean of Population Density:", round(mean_den, 2))
        print("Median of Population Density:", round(median_den, 2))
        print("Standard Deviation of Population Density:", round(std_dev_den, 2))
        
        print("\nNumber of countries who are UN Members:", un_members)
        print("Number of countries who use Euro as a currency:", euro_users)

if __name__ == "__main__":
    main()