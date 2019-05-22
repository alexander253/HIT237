from django.shortcuts import render
from .cars import Car



def home(request):
    return render(request, 'assignment_app/base.html')

#I realised I spelt calatlogue wrong throughout the whole project only at the very end.
#So I just changed the spelling where it is actually viewed on the site.
def catalouge(request):
    car_list= create_cars()
    context_data= {
        'car_list': car_list,
    }
    return render(request, 'assignment_app/catalouge.html', context_data)

def index(request):
    page_data = {
    }
    return render(request,'assignment_app/index.html', page_data)

def data(request):
    page_data = {
    }
    return render(request,'assignment_app/data.html', page_data)


def car_single(request, id):
    id = int(id)
    car_list1 = create_cars()
    car = None
    s_package= None
    for item in car_list1:
        if item.id == id:
            car = item
    page_data = {
        'car_list1': car_list1,
        'car': car,
        'id': id,
        's_package':s_package,
    }
    print(car.name)
    return render(request, 'assignment_app/cars.html', page_data)

#Function that appends objects to a list and returns that list
def create_cars():
    car_list2 = []
    car_list2.append(Car(1,"Lamborghini","italy", "12", "aventador", "2018", True,"Release the raging bull within!","In 1963, when the company was founded, it first manufactured tractors for several years"))
    car_list2.append(Car(2,"ferrari","italy", "8", "458 italia","2015",False,"Ride away on your new italian stalion!","THE 'PRANCING HORSE' LOGO IS A NOD TO AN ITALIAN FLYING ACE OF WORLD WAR 1"))
    car_list2.append(Car(3,"koenigsegg","sweden", "8", "agera rs","2017",True, "Don't let this sleek ride get away!", "Christian von Koenigsegg, founder of the Koenigsegg company was only 22 years old when he founded the company in 1994"))
    car_list2.append(Car(4,"audi","german", "10", "R8","2018",True,"These four rings are the best type!","The Auto Union/Audi produced a race car that went over 268 mph way back in 1938! "))
    car_list2.append(Car(5,"lexus","japan", "10", "LFA","2012",False,"Listen to this engine co- created by yamaha!"," there was only 500 LFA's ever created in the whole world!"))

    return car_list2
