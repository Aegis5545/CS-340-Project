from animal_shelter import AnimalShelter

animals = AnimalShelter()

print("111")

# Test Create
result = animals.create({
    "age_upon_outcome": "2 years",
    "animal_id": "42",
    "animal_type": "Dog",
    "color": "white",
    "name": "Max",
    "outcome_type": "Transfer"
})
print("Create Result:", result)

# Test Read
query = animals.read({"name": "Max"})
print("Read Result:", query)

# Test Update
update_result = animals.update({"name": "Max"}, {"outcome_type": "Adopted"})
print("Update Result:", update_result)

# Test Delete
delete_result = animals.delete({"name": "Max"})
print("Delete Result:", delete_result)
