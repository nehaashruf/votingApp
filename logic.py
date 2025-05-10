class VotingApp:
    def __init__(self, ui):
        self.ui = ui
        self.voted_ids = set()
        self.jane_votes = 0
        self.john_votes = 0
        #connectsubmitbutton
        self.ui.submitButton.clicked.connect(self.submit_vote)

    def submit_vote(self):
        #getinputvalues
        voter_id = self.ui.idInput.text().strip()
        candidate = None
        if self.ui.janeRadio.isChecked():
            candidate = "Jane"
        elif self.ui.johnRadio.isChecked():
            candidate = "John"

        #validateinput
        if not voter_id or not candidate:
            self.ui.messageLabel.setText("please enter id and select a candidate")
            return

        #checkduplicatevote
        if voter_id in self.voted_ids:
            self.ui.messageLabel.setText("this id has already voted")
            return

        #storevoteinmemory
        self.voted_ids.add(voter_id)
        if candidate == "Jane":
            self.jane_votes += 1
        else:
            self.john_votes += 1

        #savevotetofile
        try:
            with open("voters.txt", "a") as file:
                file.write(f"{voter_id},{candidate}\n")
        except Exception as e:
            self.ui.messageLabel.setText(f"error writing to file: {str(e)}")
            return

        #confirmationmessage
        self.ui.messageLabel.setText(f"vote submitted for {candidate}")
