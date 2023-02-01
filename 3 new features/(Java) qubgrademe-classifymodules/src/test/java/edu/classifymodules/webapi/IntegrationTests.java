package edu.classifymodules.webapi;

import edu.classifymodules.webapi.classifymodules.Modules;
import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
class IntegrationTests {
	@Autowired
	private MockMvc mvc;
	@Test
	void PostAllValuesAsDifferentClassifications() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": 70, \"m2_grade\": 60, \"m3_grade\": 50, \"m4_grade\": 40, \"m5_grade\": 30}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isOk())
			.andReturn();
		JSONObject obj = new JSONObject(result.getResponse().getContentAsString());

		assertEquals("1st", obj.getString("m1_grade"));
		assertEquals("2:1", obj.getString("m2_grade"));
		assertEquals("2:2", obj.getString("m3_grade"));
		assertEquals("3rd", obj.getString("m4_grade"));
		assertEquals("Failed", obj.getString("m5_grade"));
	}

	@Test
	void PostOneValueAsStringEmpty() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": \"\"}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isBadRequest())
			.andReturn();

		assertEquals("Error: To use functionality, please enter at least one mark.",
				result.getResponse().getContentAsString());
	}

	@Test
	void PostOneValueAsSpacedString() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": \"   \"}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isBadRequest())
			.andReturn();

		assertEquals("Module 1 value cannot be empty space.\n",
				result.getResponse().getContentAsString());
	}

	@Test
	void PostOneValueAsWordString() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": \"I am a string.\"}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isBadRequest())
			.andReturn();

		assertEquals("Module 1 value is not a number.\n",
				result.getResponse().getContentAsString());
	}

	@Test
	void PostMixedWordInResults() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": 70, \"m2_grade\": \"Cheese\", \"m3_grade\": 50, \"m4_grade\": \"Cheese\", \"m5_grade\": 30}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isBadRequest())
			.andReturn();

		assertEquals("Module 2 value is not a number.\n"
						+ "Module 4 value is not a number.\n",
				result.getResponse().getContentAsString());
	}

	@Test
	void PostOneValueInUpperBounds() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": 100}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isOk())
			.andReturn();
		JSONObject obj = new JSONObject(result.getResponse().getContentAsString());

		assertEquals("1st", obj.getString("m1_grade"));
	}

	@Test
	void PostOneValueInLowerBounds() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": 0}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isOk())
			.andReturn();
		JSONObject obj = new JSONObject(result.getResponse().getContentAsString());

		assertEquals("Failed", obj.getString("m1_grade"));
	}

	@Test
	void PostOneValueOutUpperBounds() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": 101}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isBadRequest())
			.andReturn();

		assertEquals("Module 1 value must be within the range of 0 to 100 to be classified.\n",
				result.getResponse().getContentAsString());
	}

	@Test
	void PostOneValueOutLowerBounds() throws Exception {
		MvcResult result = mvc.perform(post("/")
			.content("{\"m1_grade\": -1}")
			.contentType(MediaType.APPLICATION_JSON)
			.accept(MediaType.APPLICATION_JSON))
			.andExpect(status().isBadRequest())
			.andReturn();

		assertEquals("Module 1 value must be within the range of 0 to 100 to be classified.\n",
				result.getResponse().getContentAsString());
	}
}
