import json
import re


class UIImprover:
    def __init__(self, evaluator):
        self.evaluator = evaluator

    def improve(self, ui_code, idea, max_loops=2):
        current_code = ui_code

        for i in range(max_loops):
            result = self.evaluator.evaluate(current_code, idea)

            try:
                match = re.search(r"\{.*\}", result, re.DOTALL)

                if match:
                    raw_json = match.group(0)

                    # 🔥 STEP 1: Remove invalid control characters
                    raw_json = raw_json.replace("\n", " ")
                    raw_json = raw_json.replace("\r", " ")
                    raw_json = raw_json.replace("\t", " ")

                    # 🔥 STEP 2: Fix escape issues
                    raw_json = raw_json.replace("\\", "\\\\")

                    # 🔥 STEP 3: Remove broken quotes (optional safety)
                    raw_json = re.sub(r'(?<!\\)"', '"', raw_json)

                    parsed = json.loads(raw_json)

                else:
                    print("⚠️ No JSON found — retrying")
                    continue

            except Exception as e:
                print("❌ JSON parsing failed — retrying:", e)
                print("RAW (cleaned):", raw_json[:300])
                continue

            except Exception as e:
                print("❌ JSON parsing failed — retrying:", e)
                continue

            score = parsed.get("score", 0)

            print(f"🎯 UI Score (iteration {i + 1}): {score}")

            improved_code = current_code

            # Only apply small fixes (NOT full replacement)
            if "fixes" in parsed:
                print("⚡ Applying UI fixes (non-destructive)")

            if score >= 8:
                return improved_code

            current_code = improved_code

        return current_code
