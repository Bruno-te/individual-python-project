class Assignment:
    def __init__(self, name, assignment_type, score, weight):
        """
        Initializes an assignment object.

        :constant name: Name of the assignment (string)
        :constant assignment_type: Type of the assignment (Formative/Summative)
        :constant score: The student's score for the assignment (float)
        :costant weight: The weight this assignment contributes to its respective group total (float)
        """
        self.name = name
        self.assignment_type = assignment_type
        self.score = score
        self.weight = weight

    def weighted_score(self):
        """
        Calculate the weighted score for the assignment.
        :return: Weighted score as a float
        """
        return self.score * (self.weight / 100)


class Student:
    def __init__(self, name):
        """
        Initializes a student object.

        :constant name: Name of the student (string)
        """
        self.name = name
        self.assignments = []

    def add_assignment(self, assignment):
        """
        Add an assignment to the student.

        :constant assignment: An instance of the Assignment class
        """
        self.assignments.append(assignment)

    def calculate_group_score(self, assignment_type):
        """
        Calculate the total weighted score for a given assignment type (Formative/Summative).

        :constant assignment_type: Type of the assignment (Formative or Summative)
        :return: Total weighted score as a float
        """
        total_weight = 0
        weighted_score = 0
        for assignment in self.assignments:
            if assignment.assignment_type == assignment_type:
                weighted_score += assignment.weighted_score()
                total_weight += assignment.weight
        return weighted_score / total_weight if total_weight > 0 else 0

    def check_progression(self):
        """
        Check if the student passes or fails based on Formative and Summative group scores.

        :return: A message about the student's progression
        """
        formative_score = self.calculate_group_score('Formative')
        summative_score = self.calculate_group_score('Summative')

        if formative_score >= 30 and summative_score >= 20:
            return "Passed"
        else:
            return "Failed"

    def resubmission_eligible(self):
        """
        Check for Formative assignments with scores below 50% that are eligible for resubmission.

        :return: A list of assignments eligible for resubmission
        """
        return [assignment for assignment in self.assignments if assignment.assignment_type == 'Formative' and assignment.score < 50]

    def generate_transcript(self, order='ascending'):
        """
        Generate the transcript of all assignments sorted by score in the specified order.

        :constant order: Order to display the transcript, either 'ascending' or 'descending'
        :return: None, but prints the formatted transcript
        """
        # Validate order input
        if order not in ['ascending', 'descending']:
            print("Invalid input for sorting order. Defaulting to 'ascending'.")
            order = 'ascending'

        # Sort assignments
        sorted_assignments = sorted(self.assignments, key=lambda x: x.score, reverse=(order == 'descending'))

        # Print the header
        print(f"\nTranscript Breakdown ({order.capitalize()} Order):")
        print(f"{'Assignment':<20} {'Type':<12} {'Score(%)':<10} {'Weight (%)'}")
        print('-' * 50)

        # Print the assignment details
        for assignment in sorted_assignments:
            print(f"{assignment.name:<20} {assignment.assignment_type:<12} {assignment.score:<10} {assignment.weight}")
        print('-' * 50)
