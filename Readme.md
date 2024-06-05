## Quick start
### 1. Clone this [repo](https://github.com/project-kessel/relations-api) and run

```
make rebac
```

### 2. Create python environment
```
VENV_DIR=./python_grpc_venv
mkdir -p $VENV_DIR
python3 -m venv $VENV_DIR
. $VENV_DIR/bin/activate
```

### 3. Install [grpc python client](https://pypi.org/project/relations-grpc-clients-python-kessel-project/) for [Kessel relation api](https://github.com/project-kessel/relations-api)

```
pip install relations-grpc-clients-python-kessel-project
```

### 4. Test it!

```
python  client.py
```
output:
```
--Start of CreateTuples--

--End of CreateTuples--

--Start of ReadTuples--
Resource ID: bob_club
Resource Type: group
Relation: member
Subject Type: user
Subject Type: bob
--End of ReadTuples--

--Start of Check request--
allowed
--End of Check request--

--Start of LookupService--
Subject ID: bob
Resource Type: user
--End of LookupService--
```
