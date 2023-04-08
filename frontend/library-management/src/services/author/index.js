import { getAllAuthors } from "./get-all-authors";
import { newAuthor } from "./new-author";
import { updateAuthor } from './update-author';

const AuthorServices = {
    getAllAuthors,
    newAuthor,
    updateAuthor
}

export { AuthorServices };