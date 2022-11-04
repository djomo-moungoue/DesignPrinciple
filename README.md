`Python : Exemples illustrant l'application des principes de conception`

# [SOLID : Coding in Python](https://towardsdatascience.com/solid-coding-in-python-1281392a6a94)
Habituellement, les principes SOLID sont appliqués dans le contexte de la conception orientée objet (par exemple, 
les classes de Python). Le principe de `SOLID` est composé des 5 principes suivants :
- [x] `SRP` : The Single-Responsibility Principle - le principe de responsabilité unique
  - Ce principe stipule qu'**"une `classe` ne doit avoir qu'une seule raison de changer"**.
  - En d'autres termes, chaque composant de votre code (en général une classe, mais aussi une fonction) doit avoir une 
    et une seule responsabilité. En conséquence, il ne devrait y avoir qu'une seule raison de le modifier.
- [ ] `OCP` : The Open-Closed Principle - Le principe de l'ouverture et de la fermeture
  - Ce principe stipule que **"les `entités logicielles` (classes, modules, fonctions, etc.) doivent être ouvertes à 
    l'extension, mais fermées à la modification"**
  - En d'autres termes : Vous ne devriez pas avoir à modifier le code que vous avez déjà écrit pour accueillir une 
  nouvelle fonctionnalité, mais simplement ajouter ce dont vous avez maintenant besoin.
  - Cela ne signifie pas que vous ne pouvez pas modifier votre code lorsque les prémisses du code doivent être modifiées, 
    mais que si vous devez ajouter de nouvelles fonctions similaires à celle qui est présente, vous ne devriez pas avoir 
    besoin de modifier d'autres parties du code.
- [ ] `LSP` : The Liskov Substitution Principle - le principe de substitution de Liskov
  - Selon ce principe "Les `classes dérivées ou enfants` doivent être substituables à leurs classes de base ou parents". 
  - Ce principe garantit que toute classe qui est l'enfant d'une classe parent doit pouvoir être utilisée à la place de 
    son parent sans comportement inattendu. 
  - **Exemple** : [parent Rectangle] <-- [enfant Carré] 
- [ ] `ISP` : The Interface Segregation Principle - Le principe de ségrégation d'interface
  - Elle stipule que "ne pas forcer un client à mettre en œuvre une interface qui n'est pas pertinente pour lui". 
  - Ici, votre objectif principal est d'éviter les interfaces trop lourdes et de donner la préférence à de nombreuses 
    petites interfaces spécifiques au client. 
  - Vous devriez préférer de nombreuses interfaces client plutôt qu'une interface générale et chaque interface devrait 
    avoir une responsabilité spécifique. 
  - L'utilisation de ce principe permet de réduire les effets secondaires et la fréquence des changements nécessaires. 
  - **Exemple** : Un végétarien qui entre dans un restaurant aimerait avoir une carte de menu comprenant uniquement des 
    repas végétariens et une carte de menu contenant les repas végétariens et des repas non-végétariens, par ce qu'il
    n'a pas du tout besoin de savoir le repas non végétarien au menu. 
- [ ] `DiP` : The Dependency inversion Principle - Le principe d'inversion de dépendance
  - Ce principe stipule que :
    + "Les modules/classes de haut niveau ne devraient pas dépendre des modules/classes de bas niveau. Les deux doivent 
      dépendre d'abstractions".
    + "Les abstractions ne doivent pas dépendre des détails. Les détails doivent dépendre des abstractions."

# [CQS : Command Query Seperation](https://en.wikipedia.org/wiki/Command%E2%80%93query_separation)
Le principe de séparation commande-requête stipule que chaque méthode doit être soit une `commande qui exécute une action`, 
soit une `requête qui renvoie des données` à l'appelant, mais pas les deux.

# [DRY : Don't Repeat Yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
+ Le principe DRY stipule que "chaque élément de connaissance doit avoir une représentation unique, non ambiguë et
  faisant autorité au sein d'un système".
+ "Don't repeat yourself" (DRY) est un principe de développement logiciel visant à réduire la répétition des patrons
  logiciels, en les remplaçant par des abstractions ou en utilisant la normalisation des données pour éviter la redondance.
+ [Bon et mauvais exemple](https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee)

# KISS : Keep It Simple Stupid
+ Le principe KISS stipule que chaque `méthode`, `classe`, `interface` doit avoir un nom aussi clair que possible et que
  la logique à l'intérieur des fonctions, des méthodes, etc. doit être aussi claire et simple que possible.
+ le principe KISS s'implémente soit :
  + soit via l'`héritage` des attributs, des méthodes de la classe de base
  + soit via la `composition`
+ [Bon et mauvais exemple](https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee)

# [SoC : Separation of Concern](https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee)
+ Ce principe nous dit de séparer la responsabilité d'une seule classe à cette classe et à cette classe seulement.
+ Les objets ne doivent pas partager ce qu'ils font.
+ Chaque classe doit être unique et séparée des autres.

# [YAGNI : You Ain't Gonna Need It](https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee)
+ Ce principe ne nous dit pas comment faire quelque chose en code directement, mais plutôt comment coder efficacement.
+ En général, il dit que nous ne devons coder que les choses qui nous sont demandées à ce moment précis.
+ Par exemple, si nous devons valider les champs "e-mail" et "mot de passe", nous ne devons pas valider le nom, car 
  nous n'en aurons peut-être jamais besoin.
+ C'est un peu comme le TDD : nous n'écrivons des tests que pour les micro-fonctionnalités et nous écrivons le minimum 
  de code nécessaire pour travailler dessus.
+ L'`objectif de YAGNI` est de nous faire gagner du temps et de nous concentrer sur les choses les plus importantes de 
  notre `sprint`.
