from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, "index.html")

def process_money(request):
    # identified what action I will do
    game = request.POST['ihidden']

    # randomize and added current gold
    gold = get_randomize_game(game)
    request.session['gold'] += gold

    # build string game and add text to list
    sessionList = request.session['activities']
    sessionList.append(build_text(game, gold))
    request.session['activities'] = sessionList

    # del request.session['activities']
    # del request.session['gold']
    # return redirect("/")
    return render(request, "index.html")

def get_randomize_game(game):
    if game == "farm":
        return random.randint(10, 20)

    elif game == "cave":
        return random.randint(5, 10)

    elif game == "house":
        return random.randint(2, 5)

    elif game == "casino":
        return random.randint(-50, 50)

def build_text(game, gold):
    # build date time
    date_time = datetime.datetime.now()
    date_time = date_time.strftime("%Y/%m/%d %H:%M")

    text = (f"Earned {gold} golds from the {game}! ({date_time})")

    if gold <= 0:
        gold = gold * -1
        text = (f"Entered a casino and lost {gold} golds... Ouch... ({date_time})")

    return text







