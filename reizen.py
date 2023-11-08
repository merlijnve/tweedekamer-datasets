import tkapi
import csv

def fdate(date):
    if date is None:
        return ""
    else:
        return date.strftime('%Y-%m-%d')

def main():
    api = tkapi.TKApi()
    file = open("reizen.csv", "w", newline="")
    writer = csv.writer(file)
    personen = api.get_personen()
    
    fields = ["naam", "functie", "geslacht", "geboortedatum", "overlijdensdatum", "doel", "bestemming", "van", "tot_en_met", "betaald_door"]
    writer.writerow(fields)
    for p in personen:
        print(p)
        for r in p.reizen:
            writer.writerow([p.__str__(), p.functie, p.geslacht, fdate(p.geboortedatum), fdate(p.overlijdensdatum), r.doel, r.bestemming, fdate(r.van), fdate(r.tot_en_met), r.betaald_door])


if __name__ == "__main__":
    main()
