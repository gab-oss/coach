# LL4 - Coach, ViZDoom

## Repozytorium Coach:
https://github.com/IntelLabs/coach

## Instalacja
Zalecane: Ubuntu 18.04 + Python 3.6 
1. Instalacja Coach zgodnie z instrukcją w jego README, instalacja ffmpeg zamiast libav-tools
2. Aktywacja virtualenv
3. Instalacja VizDoom zgodnie z https://github.com/mwydmuch/ViZDoom w sekcji "Ubuntu"
4. Zmienna środowiskowa VIZDOOM_ROOT jest ustawiana w używanych później skryptach shell i nie powinna wymagać zmiany


## Uruchamianie:

### Testy ze zmianami parametrów Rainbow i QR DQN

cd LL4

bash rainbow_parameters_test_suite.sh

bash qr_dqn_parameters_test_suite.sh

### Testy dla obu algorytmów z domyślnymi parametrami na różnych poziomach

cd LL4 

bash set_scenarios.sh - ładuje konfigurację czterech używanych poziomów gry do odpowiedniego katalogu w folderze ViZDooma (coach_env/lib/python3.6/site-packages/vizdoom/scenarios)

bash compare_on_different_levels.sh - uruchamia przebiegi dla presetów Doom_Basic_Rainbow i Doom_Basid_QR_DQN na poziomach: BASIC, DEATHMATCH, BASCI_MOD, DEATHMATCH_MOD

### Wizualizacja

Ze względu na problemy dashboardem (brak legendy przy wczytywaniu całego katalogu, błędy przy wczytywaniu katalogu), wizualizację wykonywaliśmy w następujący sposób:

cd LL4/experiments

1. bash move.sh - tworzy w każdym typie eksperymentu (np. LL4/experiments/rainbow_discount_11_100_11) katalog "results" ze zgromadzonymi plikami csv z każdego przebiegu; po przejściu do katalogu "results" należy uruchomić z konsoli dashboard i wybrać po kolei ("Select file") pliki z folderu, który pierwszy się otworzy. Każdy plik z wynikami nazywa się tak, jak jego oryginalny folder. W przypadku testów ze zmianami parametrów algorytmów w nazwie jest data i godzina uruchomienia, dlatego kolejne, posortowane pliki będą zawierały wyniki testów w takiej kolejności, w jakiej zostały wykonane w danym typie eksperymentu (testy są zdefiniowane w LL4/[nazwa algorytmu]_parameters_test_suite.sh), czyli zazwyczaj z coraz większymi wartościami zmienianych parametrów.

2. bash move_levels_results.sh - podobny do poprzedniego, gromadzi wyniki z eksperymentów dla algorytmów z domyślnymi parametrami na różnych poziomach w folderze LL4/experiments/levels_results