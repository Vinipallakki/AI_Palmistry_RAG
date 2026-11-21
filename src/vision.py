# ======================================================
# Imports
# ======================================================

import base64
import json

from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
    VISION_MODEL,
)

# ======================================================
# PalmVisionAnalyzer
# ======================================================

class PalmVisionAnalyzer:
    """
    Analyze uploaded palm images using OpenAI Vision.
    Returns structured JSON for downstream RAG
    and PDF report generation.
    """

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

# ======================================================
# Encode Image
# ======================================================

    def _encode_image(
        self,
        image_path: str,
    ) -> str:

        with open(
            image_path,
            "rb"
        ) as image:

            return base64.b64encode(

                image.read()

            ).decode(
                "utf-8"
            )

# ======================================================
# Analyze Palm
# ======================================================

    def analyze_palm(
        self,
        image_path: str,
    ) -> dict:

        image_base64 = self._encode_image(
            image_path
        )

        print("Step 1 : Calling OpenAI Vision...")

        response = self.client.chat.completions.create(

            model=VISION_MODEL,

            response_format={
                "type": "json_object"
            },

            messages=[

                {
                    "role": "system",

                    "content": """
You are an expert Palm Image Analyzer.

Your responsibility is ONLY to describe what is visually observable.

Rules:

- Never guess.
- Never infer.
- Never identify LEFT or RIGHT hand.
- Never identify specific fingers.
- Never infer gender.
- Never predict the future.
- Never interpret palmistry meanings.
- Mention only what is clearly visible.
- If jewelry is visible, simply say:
  "A metallic ring is visible on one finger."
- If you are uncertain about any observation,
  say it cannot be determined.

Return ONLY valid JSON.

Return JSON EXACTLY in this format:

{
    "image_quality":"",
    "can_analyze":true,
    "reason":"",
    "life_line":"",
    "head_line":"",
    "heart_line":"",
    "fate_line":"",
    "sun_line":"",
    "marriage_lines":"",
    "mounts":"",
    "additional_observations":""
}
"""
                },

                {

                    "role": "user",

                    "content":[

                        {

                            "type":"text",

                            "text":"""
Analyze ONLY the uploaded palm image.

Identify:

1. Image Quality.

2. Can the palm be analyzed?

3. If analysis is not possible,
   explain the reason.

4. Describe the Life Line.

5. Describe the Head Line.

6. Describe the Heart Line.

7. Describe the Fate Line.

8. Describe the Sun Line.

9. Describe the Marriage Lines.

10. Describe the visible Mounts.

11. Mention only additional observations that are clearly visible.

Rules:

- Do NOT identify LEFT or RIGHT hand.
- Do NOT identify specific fingers.
- Do NOT infer gender.
- Do NOT guess.
- If jewelry is visible, simply state:
  "A metallic ring is visible on one finger."
- Mention only directly observable features.
- Return ONLY valid JSON.
"""
                        },

                        {

                            "type":"image_url",

                            "image_url":{

                                "url":f"data:image/jpeg;base64,{image_base64}"

                            }

                        }

                    ]

                }

            ]

        )

        print("Step 2 : OpenAI Response Received")

        result = json.loads(

            response.choices[0].message.content

        )

# ======================================================
# Validate JSON
# ======================================================

        print("Step 3 : JSON Parsed Successfully")

        result.setdefault(
            "image_quality",
            "Unknown"
        )

        result.setdefault(
            "can_analyze",
            False
        )

        result.setdefault(
            "reason",
            ""
        )

        result.setdefault(
            "life_line",
            "Not Visible"
        )

        result.setdefault(
            "head_line",
            "Not Visible"
        )

        result.setdefault(
            "heart_line",
            "Not Visible"
        )

        result.setdefault(
            "fate_line",
            "Not Visible"
        )

        result.setdefault(
            "sun_line",
            "Not Visible"
        )

        result.setdefault(
            "marriage_lines",
            "Not Visible"
        )

        result.setdefault(
            "mounts",
            "Not Visible"
        )

        result.setdefault(
            "additional_observations",
            ""
        )


# ======================================================
# Generate Summary
# ======================================================

        summary = f"""
Palm Image Analysis Summary

Image Quality:
{result['image_quality']}

Can Analyze:
{result['can_analyze']}

Reason:
{result['reason']}

Life Line:
{result['life_line']}

Head Line:
{result['head_line']}

Heart Line:
{result['heart_line']}

Fate Line:
{result['fate_line']}

Sun Line:
{result['sun_line']}

Marriage Lines:
{result['marriage_lines']}

Mounts:
{result['mounts']}

Additional Observations:
{result['additional_observations']}
"""

        result["summary"] = summary


# ======================================================
# Return Result
# ======================================================

        return result

