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
b''
End of CreateRelationshipsRequest
Start of ReadRelationshipsRequest
relationships {
  object {
    type: "group"
    id: "bob_club"
  }
  relation: "member"
  subject {
    object {
      type: "user"
      id: "bob"
    }
  }
}

End of ReadRelationshipsRequest
```
