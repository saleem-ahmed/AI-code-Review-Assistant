from ui.components import *
from ui.uploader import upload_section

from utils.file_handler import read_uploaded_file
from utils.folder_handler import read_project

from services.review_service import ReviewService

import streamlit as st


def show_home():

    page_header()

    feature_cards()

    statistics()

    option, data = upload_section()

    review_service = ReviewService()

    if option == "Upload File":

        if data:

            file = read_uploaded_file(data)

            result = review_service.prepare_review(
                file["filename"],
                file["code"],
            )

            show_result(file, result)

    elif option == "Upload Project":

        if data:

            project = read_project(data)

            st.success(
                f"{len(project)} files loaded."
            )

    else:

        if data:

            result = review_service.prepare_review(
                "Pasted Code",
                data,
            )

            show_text_result(data, result)


from ui.results import (
    show_result,
    show_text_result,
)