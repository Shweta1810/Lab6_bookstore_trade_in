
import pytest

from bookstore_trade_in import (
    process_book_buybacks,
    inspect_scanner_calibration
)

# =====================================
# PROCESS BOOK BUYBACKS TEST CASES
# =====================================

def test_single_paperback_good():
    batches = [{
        "intake_approved": True,
        "format": "paperback",
        "payout_in_credit": False,
        "books": [
            {"missing_pages": 0, "condition": "good",
             "counterfeit": False}
        ]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 8.0
    assert result["status"] == "COMPLETED"

def test_textbook_mint():
    batches = [{
        "intake_approved": True,
        "format": "textbook",
        "books": [
            {"condition": "mint", "missing_pages": 0}
        ]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 50.0

def test_hardcover_poor():
    batches = [{
        "intake_approved": True,
        "format": "hardcover",
        "books": [
            {"condition": "poor", "missing_pages": 0}
        ]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 6.0

def test_unapproved_batch():
    batches = [{
        "intake_approved": False,
        "format": "paperback",
        "books": [{"condition": "good"}]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 0.0
    assert result["status"] == "ZERO_CREDIT"

def test_invalid_format():
    batches = [{
        "intake_approved": True,
        "format": "magazine",
        "books": []
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 0.0
    assert result["status"] == "ZERO_CREDIT"

def test_missing_pages():
    batches = [{
        "intake_approved": True,
        "format": "paperback",
        "books": [
            {"missing_pages": 2, "condition": "good"}
        ]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["status"] == "ZERO_CREDIT"

def test_counterfeit_paperback():
    batches = [{
        "intake_approved": True,
        "format": "paperback",
        "books": [
            {"counterfeit": True, "condition": "good"}
        ]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 0.0

def test_counterfeit_textbook():
    batches = [{
        "intake_approved": True,
        "format": "textbook",
        "books": [
            {"counterfeit": True},
            {"condition": "mint"}
        ]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 0.0

def test_store_credit_bonus():
    batches = [{
        "intake_approved": True,
        "format": "paperback",
        "payout_in_credit": True,
        "books": [
            {"condition": "good"}
        ]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 13.0

def test_zero_credit():
    result = process_book_buybacks([], 5.0)

    assert result["total_payout"] == 0.0
    assert result["status"] == "ZERO_CREDIT"

def test_audit_rejected():
    batches = [{
        "intake_approved": True,
        "format": "paperback",
        "books": [
            {"missing_pages": 1},
            {"missing_pages": 1},
            {"missing_pages": 1},
            {"missing_pages": 1},
            {"missing_pages": 1}
        ]
    }]

    result = process_book_buybacks(batches, 5.0)

    assert result["status"] == "AUDIT_REJECTED"

def test_invalid_batches():
    with pytest.raises(ValueError):
        process_book_buybacks("invalid", 5.0)

def test_negative_bonus():
    with pytest.raises(ValueError):
        process_book_buybacks([], -5.0)

# =====================================
# SCANNER CALIBRATION TEST CASES
# =====================================

def test_scanner_no_data():
    assert inspect_scanner_calibration([]) == "NO_DATA"

def test_scanner_recalibration():
    matrix = [
        [2, 6, 7, 3]
    ]

    assert inspect_scanner_calibration(matrix) == "RECALIBRATE"

def test_scanner_calibrated():
    matrix = [
        [2, 3, 4, 5]
    ]

    assert inspect_scanner_calibration(matrix) == "CALIBRATED"

def test_scanner_streak_reset():
    matrix = [
        [6, 5, 7]
    ]

    assert inspect_scanner_calibration(matrix) == "CALIBRATED"

def test_scanner_multiple_devices():
    matrix = [
        [2, 6, 3],
        [1, 2, 3]
    ]

    assert inspect_scanner_calibration(matrix) == "CALIBRATED"
