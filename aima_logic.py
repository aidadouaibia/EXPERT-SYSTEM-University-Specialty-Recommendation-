from aima3.utils import expr
from aima3.logic import FolKB, fol_fc_ask

# Define the knowledge base
kb = FolKB()

#SCIENTIFIQUE
#science
kb.tell(expr('Possible(SciencesExpérimentales, Medecine)'))
kb.tell(expr('Possible(SciencesExpérimentales, Pharmacie)'))
kb.tell(expr('Possible(SciencesExpérimentales, MedecineDentaire)'))
kb.tell(expr('Preferable(Medecine, Sciences)'))
kb.tell(expr('Preferable(Pharmacie, Sciences)'))
kb.tell(expr('Preferable(MedecineDentaire, Sciences)'))
#Physique
kb.tell(expr('Possible(SciencesExpérimentales, SiencesPhysiques)'))
kb.tell(expr('Possible(SciencesExpérimentales, SciencesEtTechnologies)'))
#HistoireGéographique
kb.tell(expr('Possible(SciencesExpérimentales, Histoire)'))
kb.tell(expr('Possible(SciencesExpérimentales, Géographie)'))
kb.tell(expr('Possible(SciencesExpérimentales, Archéologie)'))
#SciencesIslamiques
kb.tell(expr('Possible(SciencesExpérimentales, SciencesIslamiques)'))
#Philosophie
kb.tell(expr('Possible(SciencesExpérimentales, Philosophie)'))
#Arabe
kb.tell(expr('Possible(SciencesExpérimentales, Droit)'))
kb.tell(expr('Possible(SciencesExpérimentales, LangueArabe)'))
kb.tell(expr('Possible(SciencesExpérimentales, Traducteur)'))
#Anglais
kb.tell(expr('Possible(SciencesExpérimentales, LangueAnglaise)'))
kb.tell(expr('Possible(SciencesExpérimentales, Traducteur)'))
#Français
kb.tell(expr('Possible(SciencesExpérimentales, LangueFrançaise)'))
kb.tell(expr('Possible(SciencesExpérimentales, Traducteur)'))
#Mathématiques
kb.tell(expr('Possible(SciencesExpérimentales, Mathématiques)'))
kb.tell(expr('Possible(SciencesExpérimentales, SciencesEtTechnologies)'))
kb.tell(expr('Possible(SciencesExpérimentales, Informatiques)'))
#Thamazigth
kb.tell(expr('Possible(SciencesExpérimentales, LangueAmazigh)'))


#LETTRE
#langues etrangeres 

kb.tell(expr('Possible(LanguesEtrangères, Français)'))
kb.tell(expr('Possible(LanguesEtrangères, Anglais)'))
kb.tell(expr('Possible(LanguesEtrangères, Allemand)'))
kb.tell(expr('Possible(LanguesEtrangères, Espagnole)'))
kb.tell(expr('Preferable(Traducteur, Français)'))
kb.tell(expr('Preferable(Traducteur, Anglais)'))
kb.tell(expr('Preferable(Traducteur, Allemand)'))
kb.tell(expr('Preferable(Traducteur, Espangol )'))
kb.tell(expr('Preferable(Littérature-et -civilisation -espagnole, Espangol)'))
kb.tell(expr('Preferable(Langue-et-culture-allemande, Allemand)'))
kb.tell(expr('Preferable(Littérature-et-civilisation, Français)'))
kb.tell(expr('Preferable(Langue-et-culture-française, Français)'))
kb.tell(expr('Preferable(Littérature-et-civilisation, Anglais)'))
kb.tell(expr('Preferable(Langue-et-culture-Anglaise, Anglais)'))
kb.tell(expr('Preferable(Linguistique-appliquée-et-didactique-de-la-langue-anglaise, Anglais)'))











#THE RULE
kb.tell(expr("Filière(x) & MatierePref(z) & Possible(x, y) & Preferable(y, z) ==> Result(y)"))

# Define initial facts
initial_facts = [
    expr('Filière(SciencesExpérimentales)'),
    expr('MatierePref(Français)'),
]

agenda = []

for fact in initial_facts:
    kb.tell(fact)
    agenda.append(fact)

# Working memory
memory = {}


def calculate_method(kb, agenda, memory):

 method = []

 seen = set() 
 while agenda:
    p = agenda.pop(0)
    if p in seen:
        continue  
    seen.add(p)
    if fol_fc_ask(kb, p):
        print(f'{p} is true.')
        method.append(f'{p} is true.')
        memory[p] = True
    else:
        print(f'{p} is false.')
        memory[p] = False

    # Check if new rules can be activated

    #SCIENTIFIQUE
    #science
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(Sciences)'), False):
        agenda.append(expr('Result(Medecine)'))
        agenda.append(expr('Result(Pharmacie)'))
        agenda.append(expr('Result(MedecineDentaire)'))
    if p == expr('MatierePref(Sciences)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(Medecine)'))
        agenda.append(expr('Result(Pharmacie)'))
        agenda.append(expr('Result(MedecineDentaire)'))
    #Physique
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(Physique)'), False):
        agenda.append(expr('Result(SiencesPhysiques)'))
        agenda.append(expr('Result(SciencesEtTechnologies)'))
    if p == expr('MatierePref(Physique)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(SiencesPhysiques)'))
        agenda.append(expr('Result(SciencesEtTechnologies)'))
    #HistoireGéographique
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(HistoireGéographique)'), False):
        agenda.append(expr('Result(Archéologie)'))
        agenda.append(expr('Result(Histoire)'))
        agenda.append(expr('Result(Géographie)'))
    if p == expr('MatierePref(HistoireGéographique)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(Archéologie)'))
        agenda.append(expr('Result(Histoire)'))
        agenda.append(expr('Result(Géographie)'))
    #SciencesIslamiques
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(SciencesIslamiques)'), False):
        agenda.append(expr('Result(SciencesIslamiques)'))
    if p == expr('MatierePref(SciencesIslamiques)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(SciencesIslamiques)'))
    #Philosophie
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(Philosophie)'), False):
        agenda.append(expr('Result(Philosophie)'))
    if p == expr('MatierePref(Philosophie)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(Philosophie)'))
    #Arabe
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(Arabe)'), False):
        agenda.append(expr('Result(Droit)'))
        agenda.append(expr('Result(LangueArabe)'))
        agenda.append(expr('Result(Traducteur)'))
    if p == expr('MatierePref(Arabe)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(Droit)'))
        agenda.append(expr('Result(LangueArabe)'))
        agenda.append(expr('Result(Traducteur)'))
    #Anglais
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(Anglais)'), False):
        agenda.append(expr('Result(LangueAnglaise)'))
        agenda.append(expr('Result(Traducteur)'))
    if p == expr('MatierePref(Anglais)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(LangueAnglaise)'))
        agenda.append(expr('Result(Traducteur)'))
    #Français
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(Français)'), False):
        agenda.append(expr('Result(LangueFrançaise)'))
        agenda.append(expr('Result(Traducteur)'))
    if p == expr('MatierePref(Français)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(LangueFrançaise)'))
        agenda.append(expr('Result(Traducteur)'))
    #Mathématiques
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(Mathématiques)'), False):
        agenda.append(expr('Result(Mathématiques)'))
        agenda.append(expr('Result(SciencesEtTechnologies)'))
        agenda.append(expr('Result(Informatiques)'))
    if p == expr('MatierePref(Mathématiques)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(Mathématiques)'))
        agenda.append(expr('Result(SciencesEtTechnologies)'))
        agenda.append(expr('Result(Informatiques)'))
    #Thamazigth
    if p == expr('Filière(SciencesExpérimentales)') and memory.get(expr('MatierePref(Thamazigth)'), False):
        agenda.append(expr('Result(Thamazigth)'))
    if p == expr('MatierePref(Thamazigth)') and memory.get(expr('Filière(SciencesExpérimentales)'), False):
        agenda.append(expr('Result(LangueAmazigh)'))

    #LETTRE
     #francais
    if p == expr('Filière(LanguesEtrangères)') and memory.get(expr('MatierePref(Français)'), False):
        agenda.append(expr('Result(Traducteur)'))
        agenda.append(expr('Result(Littérature-et-civilisation)'))
        agenda.append(expr('Result(Langue-et-culture-française)'))
    #Anglais
    if p == expr('Filière(Languesétrangères)') and memory.get(expr('MatierePref(Anglais)'), False):
        agenda.append(expr('Result(Traducteur)'))
        agenda.append(expr('Result(Littérature-et-civilisation)'))
        agenda.append(expr('Result(Langue-et-culture-anglaise)'))
        agenda.append(expr('Result(Linguistique-appliquée-et-didactique-de-la-langue-anglaise)'))

    #Allemand

    if p == expr('Filière(LanguesEtrangères)') and memory.get(expr('MatierePref(Allemand)'), False):
        agenda.append(expr('Result(Traducteur)'))
        agenda.append(expr('Result(Langue-et-culture-allemande)'))

    #espangol
    if p == expr('Filière(LanguesEtrangères)') and memory.get(expr('MatierePref(Espangol)'), False):
        agenda.append(expr('Result(Traducteur)'))
        agenda.append(expr('Result(Littérature-et-civilisation-espagnole)'))

 return  method


#The recommendations :
def get_recommendation(kb, memory):
    recommendations = []
    for p, value in memory.items():
        if value and p.op == 'Result':
            recommendation = f'{p.op}({p.args[0]})'
            print(recommendation)
            recommendations.append(recommendation)
    return recommendations

recommendations = get_recommendation(kb, memory)
print("Recommendations: ", recommendations)
method = calculate_method(kb, agenda, memory)
print("Method: ", method)