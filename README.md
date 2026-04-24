# UnCrackable Level 2 - Advanced Reverse Engineering Lab

Une analyse de sécurité poussée (Audit SAST et Analyse Binaire) de l'application vulnérable Android "UnCrackable Level 2". Ce projet illustre le passage de l'analyse Java à l'analyse de bibliothèques natives (C/C++) pour contourner des mécanismes de sécurité avancés.

### Fonctionnalités de l'Audit

* **Analyse de la passerelle JNI :** Décompilation de l'APK via JADX pour identifier l'externalisation de la logique de sécurité vers une bibliothèque native (`libfoo.so`).
* **Extraction & Rétro-Ingénierie Binaire :** Importation de la bibliothèque native (architecture 32-bits) dans Ghidra pour analyser le langage assembleur et le pseudo-code C.
* **Patch d'Instructions (Anti-Disassembly Bypass) :** Restauration manuelle du flux d'exécution dans Ghidra (contournement de la fonction `halt_baddata()`) pour forcer la décompilation.
* **Analyse de Mémoire (Stack Strings) :** Identification de la construction dynamique du mot de passe en mémoire.
* **Scripting de Décodage :** Création d'un script Python pour automatiser la conversion des blocs hexadécimaux selon l'architecture matérielle *Little Endian*.

### Technologies & Outils

* **Outils d'Analyse :** JADX-GUI (Décompilateur Java), Ghidra (Framework de rétro-ingénierie binaire)
* **Langages :** C/C++ (Analyse binaire), Python (Script d'automatisation), Assembleur (x86/ARM)
* **Concepts de Sécurité :** Java Native Interface (JNI), Stack Strings Obfuscation, Architecture Little Endian
* **Environnement :** Windows

### Démonstration & Rapport

Le compte-rendu détaillé de la méthodologie (analyse de `libfoo.so`, explications de l'obfuscation et manipulation sous Ghidra) est disponible directement dans le fichier `rapport.pdf`.

### Installation & Reproductibilité

Clonez le dépôt pour auditer l'application vous-même :
```cmd
git clone https://github.com/Sultan-zd/Lab5-Sec-UnCrackable2.git
```
Pour exécuter le script de décodage Little Endian depuis l'invite de commandes Windows (CMD ou PowerShell) :
```cmd
python decode_stack_strings.py
