# NETTVERKSOPPSETT

## SW1 | CISCO 3650  
**VLAN1**  
*172.16.0.4*

**GigabitEthernet1/0/1 -> R1_STUD2**  
*trunk*  
**GigabitEthernet1/0/2 -> R2_STUD2**  
*trunk*

---

## R1_STUD2 | CISCO 4221  
**gig0/0/0 -> SW1_STUD2**  
*172.16.0.2/24*  

**gig0/0/1 -> SW2_STUD2**  
*trunk*

**gig0/0/1.20**  
*10.10.20.2/24*  

**gig0/0/1.99**  
*10.10.99.12/24*

**HSRP**  
*prio 110*  
*preempt*  
*standby 1 ip 172.16.0.1*  
*standby 2 ip 10.10.20.1*  
*standby 3 ip 10.10.99.1*

**DHCP**  
*pool STUD2*  
*range 10.10.20.1–255*  
*excluded 10.10.20.1–10.10.20.99*  
*excluded 10.10.20.150–10.10.20.255*

---

## R2_STUD2 | CISCO 4221  
**gig0/0/0 -> SW1_STUD2**  
*172.16.0.3/24*

**gig0/0/1 -> SW2_STUD2**  
*trunk*

**gig0/1.20**  
*10.10.20.3/24*

**gig0/1.99**  
*10.10.99.13/24*

**HSRP**  
*prio 101*  
*standby 1 ip 172.16.0.1*  
*standby 2 ip 10.10.20.1*  
*standby 3 ip 10.10.99.1*

**DHCP**  
*pool STUD2*  
*range 10.10.20.1–255*  
*excluded 10.10.20.1–10.10.20.149*  
*excluded 10.10.20.201–10.10.20.255*

---

## SW2 | CISCO 3650  
**VLAN99**  
*10.10.99.201/24*

**GigabitEthernet1/0/1 -> R1_STUD2**  
*trunk*  
**GigabitEthernet1/0/2 -> R2_STUD2**  
*trunk*

---

## SW3 | CISCO 2960  
**VLAN99**  
*10.10.99.202/24*

**FastEthernet0/1 -> SW2_STUD2**  
*trunk*

**FastEthernet0/2-3 -> S3_STUD1**  
*EtherChannel group 1*

**FastEthernet0/4-12**  
*access VLAN 20*

**FastEthernet0/13-24**  
*access VLAN 10*

# Annbefalt mappestruktur

 ~/

├── conf.py

├──  ansible/

│    ├── hosts

│     ├── ansible.log

│     ├── home

│     └──  playbooks/

│         ├── ansible.cfg

│         ├── R1.yml

│         ├── R2.yml

│         ├── SW2.yml

│         └── SW3.yml


---

# Bruksanvisning til python scriptet (conf.py)

## Om scriptet

Python-scriptet lar deg koble til en Cisco-router eller switch via com kabel og automatisk sende konfigurasjon, inkludert IP-adresse, SSH-bruker, enable secret, VLAN og mer, alt basert på input fra brukeren.

## Forutsetninger

- Python 3.x installert
- Cisco-enheter (Router eller Switch) med konsollport
- Riktig COM-port eller `/dev/ttyUSBx` tilgjengelig

## Avhengigheter

Installer `pyserial` hvis du ikke allerede har det:

```bash
pip install pyserial
```

## Bruk

1. **Kjør scriptet** i terminal eller kommandolinje:

```bash
python3 conf.py
```

2. **Velg seriellport:**
   - På Windows: Skriv inn portnummer (f.eks. `3` for `COM3`)
   - På Linux/macOS: Skriv inn portnavn (f.eks. `S4` for `/dev/ttyS4`)

3. **Velg enhetstype:**
   - `R` for Router
   - `S` for Switch

4. **Følg instruksjonene i terminalen**:
   - Skriv inn ønsket hostname
   - Angi port, IP-adresse, VLAN, brukernavn og passord avhengig av valgt enhet
   - Velg om switchport skal være i `access` eller `trunk` modus

## Hva scriptet gjør

### Router:

* Setter hostname
* Konfigurerer management-grensesnitt med IP-adresse
* Aktiverer SSH og genererer RSA-nøkkel
* Lager lokal bruker og enable secret
* Konfigurerer VTY-linjer for SSH

### Switch:

* Lager VLAN for management
* Konfigurerer `vlan` interface med IP
* Setter trunk eller access-modus på valgt port
* Aktiverer SSH og oppretter lokal bruker
* Setter enable secret og default gateway

## Etter konfigurasjon

* Kommandoene sendes sekvensielt over konsoll
* Scriptet skriver ut responsen fra enheten
* Tilkoblingen lukkes automatisk

## Tips ved feil

* Sørg for at COM-/tty-porten er riktig og ikke er i bruk av et annet program som PuTTY (Dette har jeg gjort 10000 ganger)
* Hvis scriptet henger så kjør scriptet på nytt, kan hende du må fjerne enable secret før du kjører igjen hvis det gikk gjennom
* **DET KJØRES INGEN WRITE MEMORY VERKEN I CONF.PY ELLER I ANSIBLE SÅ IKKE RESTART ENHETER**

---

# Bruksannvisning for ANSIBLE
* Ikke så mye å si her
* Kjør med "ansible-playbook [filnavn]"
* Kjør i rekkefølge R1, R2, SW2, SW3
  
## NB!! Hvis ansible --version ikke viser filbane til ansible.cfg kjør følgende på linux (vet ikke om det funker på windows)
**export ANSIBLE_CONFIG=/filbane/til/der/du/legger/cfg**
















