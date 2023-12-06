from flask import jsonify


def response_success(data, status=200):
    return jsonify({"ok": True, "data": data}), status


def response_error(message, status=500):
    return jsonify({"ok": False, "message": message}), status
