package edu.classifymodules.webapi.classifymodules;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@CrossOrigin
@RestController
public class ClassifyModulesController {

    @PostMapping("/")
    ResponseEntity classifyModules(@RequestBody Modules request) {
        if (request.getErrorFlagged()) {
            return new ResponseEntity<>(request.getErrorMessage(), HttpStatus.BAD_REQUEST);
        } else if (request.getM1_grade() == null && request.getM2_grade() == null
                && request.getM3_grade() == null && request.getM4_grade() == null && request.getM5_grade() == null) {
            return new ResponseEntity<>("Error: To use functionality, please enter at least one mark.",
                    HttpStatus.BAD_REQUEST);
        } else {
            return ResponseEntity.ok(request);
        }
    }

}
