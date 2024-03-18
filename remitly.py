import json


def has_single_asterisk(data):
    if 'Resource' in data and data['Resource'] == '*':
        return True
    else:
        return False


def verify_input_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'PolicyDocument' in data:
                policy_document = data['PolicyDocument']
                if 'Statement' in policy_document:
                    statements = policy_document['Statement']
                    for statement in statements:
                        if has_single_asterisk(statement):
                            return False
                else:
                    print("Statement field missing in PolicyDocument.")
                    return False
            else:
                print("PolicyDocument field missing.")
                return False
            return True
    except FileNotFoundError:
        print("File not found.")
        return False
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return False


# Unit tests
def test_verify_input_json():
    # field contains a single asterisk
    assert not verify_input_json("src/test_input_json_with_asterisk.json")

    # field does not contain a single asterisk
    assert verify_input_json("src/test_input_json_without_asterisk.json")

    # PolicyDocument field is missing
    assert not verify_input_json("src/test_input_json_missing_policydocument.json")

    # statement field is missing
    assert not verify_input_json("src/test_input_json_missing_statement.json")

    # file not found
    assert not verify_input_json("src/non_existent_file.json")

    # invalid JSON format
    assert not verify_input_json("src/invalid_json.json")

    print("All tests passed successfully.")


if __name__ == "__main__":
    test_verify_input_json()
