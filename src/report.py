# ============================================================
# SECTION 1 - IMPORTS
# ============================================================

import os
import re
from datetime import datetime
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)
from reportlab.lib.units import mm

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    CondPageBreak,
)

from config.settings import REPORT_DIR

# ============================================================
# SECTION 2 - COLORS
# ============================================================

DARK_PURPLE = colors.HexColor("#10051F")
DEEP_PURPLE = colors.HexColor("#1B0B35")
CARD_PURPLE = colors.HexColor("#24134A")

LIGHT_PURPLE = colors.HexColor("#E8D9FF")
SOFT_WHITE = colors.HexColor("#F7F2FF")
MUTED = colors.HexColor("#C7B8DD")

GOLD = colors.HexColor("#F4C95D")
GOLD_LIGHT = colors.HexColor("#FFE9A8")

BORDER = colors.HexColor("#7045A8")
SOFT_BORDER = colors.HexColor("#9B6FD3")

QUESTION_BG = colors.HexColor("#2D1855")
OBSERVATION_BG = colors.HexColor("#21113F")

# ============================================================
# SECTION 3 - REPORT GENERATOR
# ============================================================

class ReportGenerator:

    def __init__(self):

        styles = getSampleStyleSheet()

        # ----------------------------------------------------
        # Main title
        # ----------------------------------------------------

        self.title_style = ParagraphStyle(
            "ReportTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=23,
            leading=28,
            alignment=TA_CENTER,
            textColor=GOLD,
            spaceAfter=6,
        )

        # ----------------------------------------------------
        # Subtitle
        # ----------------------------------------------------

        self.subtitle_style = ParagraphStyle(
            "ReportSubtitle",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            textColor=LIGHT_PURPLE,
            spaceAfter=8,
        )

        # ----------------------------------------------------
        # Section heading
        # ----------------------------------------------------

        self.heading_style = ParagraphStyle(
            "ReportHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            alignment=TA_LEFT,
            textColor=SOFT_WHITE,
            spaceAfter=0,
        )

        # ----------------------------------------------------
        # Body text
        # ----------------------------------------------------

        self.body_style = ParagraphStyle(
            "ReportBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=15,
            alignment=TA_LEFT,
            textColor=SOFT_WHITE,
            spaceAfter=7,
        )

        # ----------------------------------------------------
        # Table label
        # ----------------------------------------------------

        self.table_label_style = ParagraphStyle(
            "TableLabel",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=12,
            textColor=GOLD,
        )

        # ----------------------------------------------------
        # Table value
        # ----------------------------------------------------

        self.table_value_style = ParagraphStyle(
            "TableValue",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=13,
            textColor=SOFT_WHITE,
        )

        # ----------------------------------------------------
        # Question
        # ----------------------------------------------------

        self.question_style = ParagraphStyle(
            "Question",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=16,
            textColor=SOFT_WHITE,
        )

        # ----------------------------------------------------
        # Disclaimer
        # ----------------------------------------------------

        self.disclaimer_style = ParagraphStyle(
            "Disclaimer",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=11,
            textColor=MUTED,
        )

# ============================================================
# SECTION 4 - PAGE BACKGROUND
# ============================================================

    def draw_background(
        self,
        canvas,
        doc,
    ):

        canvas.saveState()

        # ----------------------------------------------------
        # Main background
        # ----------------------------------------------------

        canvas.setFillColor(
            DARK_PURPLE
        )

        canvas.rect(
            0,
            0,
            A4[0],
            A4[1],
            fill=1,
            stroke=0,
        )

        # ----------------------------------------------------
        # Top background panel
        # ----------------------------------------------------

        canvas.setFillColor(
            DEEP_PURPLE
        )

        canvas.rect(
            0,
            A4[1] - 35 * mm,
            A4[0],
            35 * mm,
            fill=1,
            stroke=0,
        )

        # ----------------------------------------------------
        # Top gold line
        # ----------------------------------------------------

        canvas.setStrokeColor(
            GOLD
        )

        canvas.setLineWidth(
            0.8
        )

        canvas.line(
            15 * mm,
            A4[1] - 12 * mm,
            A4[0] - 15 * mm,
            A4[1] - 12 * mm,
        )

        # ----------------------------------------------------
        # Bottom line
        # ----------------------------------------------------

        canvas.setStrokeColor(
            BORDER
        )

        canvas.line(
            15 * mm,
            12 * mm,
            A4[0] - 15 * mm,
            12 * mm,
        )

        # ----------------------------------------------------
        # Footer
        # ----------------------------------------------------

        canvas.setFont(
            "Helvetica",
            7.5,
        )

        canvas.setFillColor(
            MUTED
        )

        canvas.drawCentredString(
            A4[0] / 2,
            7 * mm,
            "Palmistry Report • Personal Observation",
        )

        canvas.restoreState()

# ============================================================
# SECTION 5 - CLEAN TEXT
# ============================================================

    def clean_text(
        self,
        text,
    ):

        if text is None:
            return ""

        text = str(
            text
        )

        # ----------------------------------------------------
        # Remove generated disclaimer section
        # ----------------------------------------------------

        text = re.split(
            r"(?im)^\s*Disclaimer\s*$",
            text,
            maxsplit=1,
        )[0]

        # ----------------------------------------------------
        # Remove internal generated headings
        # ----------------------------------------------------

        text = re.sub(
            r"(?im)^\s*#{0,6}\s*Palm Image Observation\s*$",
            "",
            text,
        )

        text = re.sub(
            r"(?im)^\s*#{0,6}\s*Palmistry Interpretation\s*$",
            "",
            text,
        )

        text = re.sub(
            r"(?im)^\s*#{0,6}\s*Final Answer\s*$",
            "",
            text,
        )

        # ----------------------------------------------------
        # Remove markdown headings
        # ----------------------------------------------------

        text = re.sub(
            r"^\s*#{1,6}\s*",
            "",
            text,
            flags=re.MULTILINE,
        )

        # ----------------------------------------------------
        # Remove markdown horizontal lines
        # ----------------------------------------------------

        text = re.sub(
            r"^\s*[-*_]{3,}\s*$",
            "",
            text,
            flags=re.MULTILINE,
        )

        # ----------------------------------------------------
        # Remove markdown bold
        # ----------------------------------------------------

        text = text.replace(
            "**",
            "",
        )

        # ----------------------------------------------------
        # Remove AI / RAG labels if generated in answer
        # ----------------------------------------------------

        text = re.sub(
            r"\bAI\b",
            "",
            text,
            flags=re.IGNORECASE,
        )

        text = re.sub(
            r"\bRAG\b",
            "",
            text,
            flags=re.IGNORECASE,
        )

        # ----------------------------------------------------
        # Remove excessive spaces
        # ----------------------------------------------------

        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        # ----------------------------------------------------
        # Remove excessive blank lines
        # ----------------------------------------------------

        text = re.sub(
            r"\n\s*\n\s*\n+",
            "\n\n",
            text,
        )

        return text.strip()


    def safe_text(
        self,
        text,
    ):

        return escape(
            self.clean_text(text)
        ).replace(
            "\n",
            "<br/>",
        )

# ============================================================
# SECTION 6 - SECTION HEADER
# ============================================================

    def section_header(
        self,
        title,
    ):

        header = Table(
            [
                [
                    Paragraph(
                        title,
                        self.heading_style,
                    )
                ]
            ],
            colWidths=[
                170 * mm
            ],
        )

        header.setStyle(
            TableStyle(
                [

                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, -1),
                        DEEP_PURPLE,
                    ),

                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        0.8,
                        GOLD,
                    ),

                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        10,
                    ),

                    (
                        "RIGHTPADDING",
                        (0, 0),
                        (-1, -1),
                        10,
                    ),

                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        7,
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        7,
                    ),
                ]
            )
        )

        return header

# ============================================================
# SECTION 7 - PALM OBSERVATION TABLE
# ============================================================

    def create_observation_table(
        self,
        vision_result,
    ):

        observations = [

            (
                "Life Line",
                vision_result.get(
                    "life_line",
                    "Not available",
                ),
            ),

            (
                "Head Line",
                vision_result.get(
                    "head_line",
                    "Not available",
                ),
            ),

            (
                "Heart Line",
                vision_result.get(
                    "heart_line",
                    "Not available",
                ),
            ),

            (
                "Fate Line",
                vision_result.get(
                    "fate_line",
                    "Not available",
                ),
            ),

            (
                "Sun Line",
                vision_result.get(
                    "sun_line",
                    "Not available",
                ),
            ),

            (
                "Marriage Lines",
                vision_result.get(
                    "marriage_lines",
                    "Not available",
                ),
            ),

            (
                "Mounts",
                vision_result.get(
                    "mounts",
                    "Not available",
                ),
            ),

            (
                "Additional Observations",
                vision_result.get(
                    "additional_observations",
                    "Not available",
                ),
            ),
        ]

        data = []

        for label, value in observations:

            data.append(
                [
                    Paragraph(
                        label,
                        self.table_label_style,
                    ),

                    Paragraph(
                        escape(
                            str(value)
                        ),
                        self.table_value_style,
                    ),
                ]
            )

        table = Table(
            data,
            colWidths=[
                45 * mm,
                125 * mm,
            ],
        )

        table.setStyle(
            TableStyle(
                [

                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, -1),
                        DEEP_PURPLE,
                    ),

                    (
                        "BACKGROUND",
                        (1, 0),
                        (1, -1),
                        OBSERVATION_BG,
                    ),

                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        0.8,
                        BORDER,
                    ),

                    (
                        "INNERGRID",
                        (0, 0),
                        (-1, -1),
                        0.35,
                        BORDER,
                    ),

                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "TOP",
                    ),

                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        9,
                    ),

                    (
                        "RIGHTPADDING",
                        (0, 0),
                        (-1, -1),
                        9,
                    ),

                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        8,
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        8,
                    ),
                ]
            )
        )

        return table

# ============================================================
# SECTION 8 - INTERPRETATION TEXT
# ============================================================

    def create_text_blocks(
        self,
        text,
    ):

        cleaned = self.clean_text(
            text
        )

        if not cleaned:
            return []

        blocks = re.split(
            r"\n\s*\n",
            cleaned,
        )

        result = []

        for block in blocks:

            block = block.strip()

            if not block:
                continue

            result.append(
                Paragraph(
                    escape(block).replace(
                        "\n",
                        "<br/>",
                    ),
                    self.body_style,
                )
            )

        return result

# ============================================================
# SECTION 9 - MAIN PDF GENERATOR
# ============================================================

    def generate(
        self,
        image_path: str,
        question: str,
        vision_result: dict,
        answer: str,
    ) -> str:

        # ----------------------------------------------------
        # Create report directory
        # ----------------------------------------------------

        os.makedirs(
            REPORT_DIR,
            exist_ok=True,
        )

        # ----------------------------------------------------
        # Create PDF filename
        # ----------------------------------------------------

        filename = (
            "Palmistry_Report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        )

        pdf_path = os.path.join(
            REPORT_DIR,
            filename,
        )

        # ----------------------------------------------------
        # PDF document
        # ----------------------------------------------------

        doc = SimpleDocTemplate(
            pdf_path,
            pagesize=A4,
            rightMargin=20 * mm,
            leftMargin=20 * mm,
            topMargin=18 * mm,
            bottomMargin=18 * mm,
            title="Palmistry Report",
            author="Palmistry Assistant",
        )

        story = []

        # ====================================================
        # REPORT HEADER
        # ====================================================

        story.append(
            Spacer(
                1,
                4,
            )
        )

        story.append(
            Paragraph(
                "PALMISTRY REPORT",
                self.title_style,
            )
        )

        story.append(
            Paragraph(
                "Personal Palm Observation & Interpretation",
                self.subtitle_style,
            )
        )

        story.append(
            Spacer(
                1,
                12,
            )
        )

        # ====================================================
        # USER INFORMATION
        # ====================================================

        story.append(
            self.section_header(
                "User Information"
            )
        )

        story.append(
            Spacer(
                1,
                8,
            )
        )

        user_data = [

            [
                Paragraph(
                    "Report Generated",
                    self.table_label_style,
                ),

                Paragraph(
                    datetime.now().strftime(
                        "%d-%b-%Y %I:%M %p"
                    ),
                    self.table_value_style,
                ),
            ],

            [
                Paragraph(
                    "Report Type",
                    self.table_label_style,
                ),

                Paragraph(
                    "Palm Analysis Report",
                    self.table_value_style,
                ),
            ],
        ]

        user_table = Table(
            user_data,
            colWidths=[
                45 * mm,
                125 * mm,
            ],
        )

        user_table.setStyle(
            TableStyle(
                [

                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, -1),
                        DEEP_PURPLE,
                    ),

                    (
                        "BACKGROUND",
                        (1, 0),
                        (1, -1),
                        CARD_PURPLE,
                    ),

                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        0.8,
                        BORDER,
                    ),

                    (
                        "INNERGRID",
                        (0, 0),
                        (-1, -1),
                        0.35,
                        BORDER,
                    ),

                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "MIDDLE",
                    ),

                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        9,
                    ),

                    (
                        "RIGHTPADDING",
                        (0, 0),
                        (-1, -1),
                        9,
                    ),

                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        8,
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        8,
                    ),
                ]
            )
        )

        story.append(
            user_table
        )

        story.append(
            Spacer(
                1,
                14,
            )
        )

        # ====================================================
        # UPLOADED PALM IMAGE
        # ====================================================

        story.append(
            self.section_header(
                "Uploaded Palm Image"
            )
        )

        story.append(
            Spacer(
                1,
                8,
            )
        )

        if image_path and os.path.exists(
            image_path
        ):

            palm_image = Image(
                image_path,
                width=72 * mm,
                height=92 * mm,
            )

            palm_image.hAlign = "CENTER"

            image_table = Table(
                [
                    [
                        palm_image
                    ]
                ],
                colWidths=[
                    170 * mm
                ],
            )

            image_table.setStyle(
                TableStyle(
                    [

                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, -1),
                            CARD_PURPLE,
                        ),

                        (
                            "BOX",
                            (0, 0),
                            (-1, -1),
                            0.8,
                            BORDER,
                        ),

                        (
                            "ALIGN",
                            (0, 0),
                            (-1, -1),
                            "CENTER",
                        ),

                        (
                            "VALIGN",
                            (0, 0),
                            (-1, -1),
                            "MIDDLE",
                        ),

                        (
                            "TOPPADDING",
                            (0, 0),
                            (-1, -1),
                            10,
                        ),

                        (
                            "BOTTOMPADDING",
                            (0, 0),
                            (-1, -1),
                            10,
                        ),
                    ]
                )
            )

            story.append(
                image_table
            )

        story.append(
            Spacer(
                1,
                14,
            )
        )

        # ====================================================
        # PALM OBSERVATION
        # ====================================================

        story.append(
            self.section_header(
                "Palm Observation"
            )
        )

        story.append(
            Spacer(
                1,
                8,
            )
        )

        observation_table = (
            self.create_observation_table(
                vision_result
            )
        )

        story.append(
            observation_table
        )

        story.append(
            Spacer(
                1,
                16,
            )
        )

        # ====================================================
        # USER QUESTION
        # ====================================================

        story.append(
            self.section_header(
                "Your Question"
            )
        )

        story.append(
            Spacer(
                1,
                8,
            )
        )

        question_box = Table(
            [
                [
                    Paragraph(
                        escape(
                            str(question)
                        ),
                        self.question_style,
                    )
                ]
            ],
            colWidths=[
                170 * mm
            ],
        )

        question_box.setStyle(
            TableStyle(
                [

                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, -1),
                        QUESTION_BG,
                    ),

                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        0.8,
                        SOFT_BORDER,
                    ),

                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        12,
                    ),

                    (
                        "RIGHTPADDING",
                        (0, 0),
                        (-1, -1),
                        12,
                    ),

                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        10,
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        10,
                    ),
                ]
            )
        )

        story.append(
            question_box
        )

        story.append(
            Spacer(
                1,
                16,
            )
        )

        # ====================================================
        # PALMISTRY INTERPRETATION
        # ====================================================

        story.append(
            CondPageBreak(
                70 * mm
            )
        )

        story.append(
            self.section_header(
                "Palmistry Interpretation"
            )
        )

        story.append(
            Spacer(
                1,
                8,
            )
        )

        answer_blocks = (
            self.create_text_blocks(
                answer
            )
        )

        # ------------------------------------------------
        # Add interpretation paragraphs directly.
        #
        # Do NOT put the entire answer inside one Table.
        # This allows ReportLab to naturally continue
        # the content onto the next page.
        # ------------------------------------------------

        for block in answer_blocks:

            story.append(
                block
            )

        story.append(
            Spacer(
                1,
                18,
            )
        )

        # ====================================================
        # DISCLAIMER
        # ====================================================

        story.append(
            CondPageBreak(
                55 * mm
            )
        )

        disclaimer = (
            "Palmistry is a traditional interpretative practice "
            "and is not scientifically validated. The observations "
            "and interpretations in this report are provided for "
            "informational and entertainment purposes only."
        )

        disclaimer_box = Table(
            [
                [
                    Paragraph(
                        "Disclaimer",
                        self.heading_style,
                    )
                ],

                [
                    Paragraph(
                        escape(
                            disclaimer
                        ),
                        self.disclaimer_style,
                    )
                ],
            ],
            colWidths=[
                170 * mm
            ],
        )

        disclaimer_box.setStyle(
            TableStyle(
                [

                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, -1),
                        DEEP_PURPLE,
                    ),

                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        0.8,
                        GOLD,
                    ),

                    (
                        "LINEBELOW",
                        (0, 0),
                        (-1, 0),
                        0.8,
                        GOLD,
                    ),

                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        10,
                    ),

                    (
                        "RIGHTPADDING",
                        (0, 0),
                        (-1, -1),
                        10,
                    ),

                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, 0),
                        8,
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, 0),
                        8,
                    ),

                    (
                        "TOPPADDING",
                        (0, 1),
                        (-1, 1),
                        10,
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 1),
                        (-1, 1),
                        10,
                    ),
                ]
            )
        )

        story.append(
            disclaimer_box
        )

        # ====================================================
        # BUILD PDF
        # ====================================================

        doc.build(
            story,
            onFirstPage=self.draw_background,
            onLaterPages=self.draw_background,
        )

        return pdf_path
    
