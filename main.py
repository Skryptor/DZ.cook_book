def Creat_List():
  list_recept =[]

  with open('recept.txt', encoding='utf-8') as f:
    Recept = f.readlines()

  for list in Recept:
    list_recept.append(list.strip())

  return list_recept
#print(Creat_List())


def Creat_Dict():
  result = {}
  Sohranylka = None

  for item in Creat_List():
    if item.isdigit():
      continue
    elif len(item.split('|')) == 1:
      Sohranylka = item
      result[Sohranylka] = []
    else:
      variable_split = item.split('|')
      ingredient_name = variable_split[0]
      quantity = variable_split[1]
      measure = variable_split[2]
      result[Sohranylka].append({
        'ingredient_name': ingredient_name,
        'quantity': quantity,
        'measure': measure
      })
  return result
#print(Creat_Dict())


def Calculate_dish_quantity(quantity,disher):
  cook_book = Creat_Dict()
  result = {}
  for dish in disher:
    if dish in cook_book:
      result[dish] = []
      for ingredient in cook_book[dish]:
        ingredient_name = ingredient['ingredient_name']
        amount = int(ingredient['quantity']) * int(quantity)
        measure = ingredient['measure']
        result[dish].append({ingredient_name: {'quantity': amount, 'measure': measure}})
    else:
      return f"Блюдо '{dish}' не найдено вCook."

  return result

#print(Calculate_dish_quantity(152,['Утка по-пекински','Омлет']))




