# Python 3 : Exemples illustrant l'application des principes de conception
- Je vous recommande d'`exécuter` les exemples pour mieux comprendre les concepts.
- J'ai `testé` ces exemples et ils fonctionnent tous comme prévu.
- `N.B.` : 
  - Tout `commentaire constructif` est le bien venu, parce que Rome n'a été construit en un seul jour. 
  - Merci d'avance !

# SOLID(SRP, OCP, LSP, ISP, DiP)
Habituellement, les principes SOLID sont appliqués dans le contexte de la conception orientée objet (par exemple, 
les classes de Python). Le principe de `SOLID` est composé des 5 principes suivants :
- [x] `SRP` : The Single-Responsibility Principle - le principe de responsabilité unique
  - Ce principe stipule qu'**"une `classe` ne doit avoir qu'une seule raison de changer"**.
  - En d'autres termes, chaque composant de votre code (en général une classe, mais aussi une fonction) doit avoir une 
    et une seule responsabilité. En conséquence, il ne devrait y avoir qu'une seule raison de le modifier.
  - Exemple : solidprincipleza.py 
- [x] `OCP` : The Open-Closed Principle - Le principe de l'ouverture et de la fermeture
  - Ce principe stipule que **"les `entités logicielles` (classes, modules, fonctions, etc.) doivent être ouvertes à 
    l'extension, mais fermées à la modification"**
  - En d'autres termes : Vous ne devriez pas avoir à modifier le code que vous avez déjà écrit pour accueillir une 
  nouvelle fonctionnalité, mais simplement ajouter ce dont vous avez maintenant besoin.
  - Cela ne signifie pas que vous ne pouvez pas modifier votre code lorsque les prémisses du code doivent être modifiées, 
    mais que si vous devez ajouter de nouvelles fonctions similaires à celle qui est présente, vous ne devriez pas avoir 
    besoin de modifier d'autres parties du code.
  - Le résultat est une classe très `flexible`, dont l'entretien nécessite un minimum de temps. 
  - Exemple : solidprincipleza.py  
- [x] `LSP` : The Liskov Substitution Principle - le principe de substitution de Liskov
  - Ce principe stipule que : "Les fonctions qui utilisent des pointeurs ou des références à des classes de base 
    doivent pouvoir utiliser des objets de classes dérivées sans le savoir".
  - En d'autres termes : "Les classes dérivées doivent être substituables à leurs classes de base".
  - En termes plus simples, si une sous-classe redéfinit une fonction également présente dans la classe parente, 
    un client-utilisateur ne devrait pas remarquer de différence de comportement, et elle est un substitut de la classe 
    de base.
  - Par exemple, si vous utilisez une fonction et que votre collègue change la classe de base, vous ne devriez pas 
    remarquer de différence dans la fonction que vous utilisez.
  - C'est le principe le plus abscons à comprendre et à expliquer parmi tous les principes SOLID. Par conséquent, il 
    n'existe pas de solution standard de type "modèle" où il doit être appliqué, et il est difficile de proposer un 
    **exemple standard** à présenter.
  - Dans l'exemple `solidprincipleza.py`, la méthode `do_operation_za` est présente dans les sous-classes `MeanZa`, 
    `MaxZa`, `MedianZa` et dans la classe de base OperationZa. L'utilisateur final doit s'attendre au même comportement 
    de la part de ces deux classes.
  - Le résultat de ce principe est que nous écrirons notre code d'une manière cohérente et, l'utilisateur final n'aura 
    besoin d'apprendre comment notre code fonctionne, qu'une seule fois.
  - Une conséquence de LSP est que : la nouvelle fonction redéfinie dans la sous-classe devrait être valide et pouvoir 
    être utilisée partout où la même fonction dans la classe parente est utilisée.
- [x] `ISP` : The Interface Segregation Principle - Le principe de ségrégation d'interface
  - Ce principe stipule que : "De nombreuses interfaces spécifiques au client sont meilleures qu'une interface générale".
  - Dans le concours des classes, on considère une interface, toutes les méthodes et propriétés "exposées", donc, 
    tout ce avec quoi un utilisateur peut interagir qui appartient à cette classe.
  - Dans ce sens, les principes de ségrégation d'interface (ISP) nous disent qu'une classe ne doit avoir que l'interface 
    nécessaire (SRP) et éviter les méthodes qui n'ont aucune raison de faire partie de cette classe.
  - Ce problème se pose principalement lorsqu'une sous-classe hérite de méthodes d'une classe de base dont elle n'a pas besoin.
  - Exemple : solidprincipleza.py  
- [ ] `DiP` : The Dependency inversion Principle - Le principe d'inversion de dépendance
  - Ce principe stipule que :
    + "Les modules/classes de haut niveau ne devraient pas dépendre des modules/classes de bas niveau. Les deux doivent 
      dépendre d'abstractions".
    + "Les abstractions ne doivent pas dépendre des détails. Les détails doivent dépendre des abstractions."
  - Exemple : solidprincipleza.py  

# CQS : Command Query Seperation
Le principe de séparation commande-requête stipule que chaque méthode doit être soit une `commande qui exécute une action`, 
soit une `requête qui renvoie des données` à l'appelant, mais pas les deux.

# DRY : Don't Repeat Yourself
+ Le principe DRY stipule que "chaque élément de connaissance doit avoir une représentation unique, non ambiguë et
  faisant autorité au sein d'un système".
+ "Don't repeat yourself" (DRY) est un principe de développement logiciel visant à réduire la répétition des patrons
  logiciels, en les remplaçant par des abstractions ou en utilisant la normalisation des données pour éviter la redondance.

# KISS : Keep It Simple Stupid
+ Le principe KISS stipule que chaque `méthode`, `classe`, `interface` doit avoir un nom aussi clair que possible et que
  la logique à l'intérieur des fonctions, des méthodes, etc. doit être aussi claire et simple que possible.
+ le principe KISS s'implémente soit :
  + soit via l'`héritage` des attributs, des méthodes de la classe de base
  + soit via la `composition`

# SoC : Separation of Concern
+ Ce principe nous dit de séparer la responsabilité d'une seule classe à cette classe et à cette classe seulement.
+ Les objets ne doivent pas partager ce qu'ils font.
+ Chaque classe doit être unique et séparée des autres.

# YAGNI : You Ain't Gonna Need It
+ Ce principe ne nous dit pas comment faire quelque chose en code directement, mais plutôt comment coder efficacement.
+ En général, il dit que nous ne devons coder que les choses qui nous sont demandées à ce moment précis.
+ Par exemple, si nous devons valider les champs "e-mail" et "mot de passe", nous ne devons pas valider le nom, car 
  nous n'en aurons peut-être jamais besoin.
+ C'est un peu comme le TDD : nous n'écrivons des tests que pour les micro-fonctionnalités et nous écrivons le minimum 
  de code nécessaire pour travailler dessus.
+ L'`objectif de YAGNI` est de nous faire gagner du temps et de nous concentrer sur les choses les plus importantes de 
  notre `sprint`.

#### Bibliographie :
+ SOLID : https://towardsdatascience.com/solid-coding-in-python-1281392a6a94
+ CQS : https://en.wikipedia.org/wiki/Command%E2%80%93query_separation
+ DRY : 
  + https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
  + https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee 
+ KISS : https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee
+ SoC : https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee
+ YAGNI : https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee

