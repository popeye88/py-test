import init_django_orm  # noqa: F401
from db.models import Car


def main():
    # car = Car.objects.create(
    #     brand="BYD",
    #     horse_power=250,
    #     creation_date="2013-11-04",
    #     # description="Kia Kia Kia",
    #     engine_type="pupa",
    # )
    # # Car.objects.filter(brand="Nissan").update(engine_type="ELECTRICAL")
    car = Car(
        brand="BYD",
        horse_power=250,
        creation_date="2013-11-04",
        # description="Kia Kia Kia",
        engine_type="pupa",
    )
    car.save()
    # print(car)


if __name__ == "__main__":
    main()
