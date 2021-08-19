import pytest

base_url = 'https://www.biofourmis.com'

def test_biofourmis_solutions_page(setUp):
		expected_h3_section_headers = ['BiovitalsHF®', 'RhythmAnalytics®', 'Biovitals® Sentinel', 'Painfocus™', "Gaido™", 'Biovitals® Research']
		expected_h2_section_headers = ['Our Product Portfolio', 'Digital therapeutics solutions for the real world']
		
		bio_fourmis = setUp
		bio_fourmis.base_page().navigate_to_url(base_url)
		bio_fourmis.solutions_page().navigate_to_solutions_page()
		assert bio_fourmis.solutions_page().is_solutions_page()
		
		actual_h3_section_headers = bio_fourmis.solutions_page().get_h3_section_headers()
		while("" in actual_h3_section_headers) :
		    actual_h3_section_headers.remove("")
		assert actual_h3_section_headers == expected_h3_section_headers

		actual_h2_section_headers = bio_fourmis.solutions_page().get_h2_section_headers()
		while("" in actual_h2_section_headers) :
		    actual_h2_section_headers.remove("")
		assert actual_h2_section_headers == expected_h2_section_headers

def test_biofourmis_aboutus_page(setUp):
		expected_h3_section_headers = ['EXECUTIVE TEAM', 'CLINICAL ADVISORY BOARD', 'COLLABORATORS', 'INVESTORS']
		expected_h2_section_headers = [
																		"We're glad you're here. Allow us to introduce ourselves.",
																		'Who we are.',
																		'Collaborators & Investors',
																		'We see great things in your future.'
																		]
		
		bio_fourmis = setUp
		bio_fourmis.base_page().navigate_to_url(base_url)
		bio_fourmis.aboutus_page().navigate_to_aboutus_page()
		assert bio_fourmis.aboutus_page().is_aboutus_page()

		actual_h3_section_headers = bio_fourmis.aboutus_page().get_h3_section_headers()
		while("" in actual_h3_section_headers) :
		    actual_h3_section_headers.remove("")
		assert actual_h3_section_headers == expected_h3_section_headers

		actual_h2_section_headers = bio_fourmis.aboutus_page().get_h2_section_headers()
		while("" in actual_h2_section_headers) :
		    actual_h2_section_headers.remove("")
		assert actual_h2_section_headers == expected_h2_section_headers






